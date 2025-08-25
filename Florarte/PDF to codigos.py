import fitz  # PyMuPDF
import re    # Expressões regulares
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import datetime

# --- Funções de Lógica (mantidas do script anterior) ---

def extract_text_from_pdf(pdf_path):
    """
    Extrai todo o conteúdo de texto de um arquivo PDF.
    """
    text = ""
    try:
        document = fitz.open(pdf_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text()
        document.close()
    except Exception as e:
        raise Exception(f"Erro ao extrair texto do PDF: {e}")
    return text

def find_product_codes(text_content):
    """
    Encontra códigos de produto no texto extraído com base em padrões específicos:
    - Exatamente 6 dígitos numéricos
    - Exatamente 8 dígitos numéricos
    - Exatamente 8 dígitos numéricos seguidos pela letra 'F' (total de 9 caracteres)
    """
    # Ordem das alternativas é importante: padrões mais específicos/longos primeiro.
    # \b garante que é uma "palavra inteira" para evitar capturas parciais.
    # \d{8}F -> 8 dígitos + 'F'
    # \d{8}  -> 8 dígitos
    # \d{6}  -> 6 dígitos
    regex_pattern = r'\b\d{8}F\b|\b\d{8}\b|\b\d{6}\b'
    
    found_codes = re.findall(regex_pattern, text_content)
    
    # Remove duplicatas e ordena
    return sorted(list(set(found_codes)))

# --- Funções da Interface Gráfica (GUI) ---

class ProductCodeExtractorApp:
    def __init__(self, master):
        self.master = master
        master.title("Extrator de Códigos de Produto do PDF")
        master.geometry("600x500") # Tamanho inicial da janela

        # Configurar grid para redimensionamento
        master.grid_rowconfigure(5, weight=1) # A linha do scrolledtext expandirá
        master.grid_columnconfigure(1, weight=1) # A coluna dos campos de entrada expandirá

        # Variáveis Tkinter para os caminhos
        self.pdf_path_var = tk.StringVar()
        self.output_dir_var = tk.StringVar()

        # --- Widgets para Seleção de PDF ---
        tk.Label(master, text="Caminho do PDF:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.pdf_entry = tk.Entry(master, textvariable=self.pdf_path_var, width=60)
        self.pdf_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        self.pdf_button = tk.Button(master, text="Selecionar PDF", command=self.browse_pdf)
        self.pdf_button.grid(row=0, column=2, padx=10, pady=5)

        # --- Widgets para Seleção de Pasta de Saída ---
        tk.Label(master, text="Pasta para Salvar:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.output_entry = tk.Entry(master, textvariable=self.output_dir_var, width=60)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        self.output_button = tk.Button(master, text="Selecionar Pasta", command=self.browse_output_dir)
        self.output_button.grid(row=1, column=2, padx=10, pady=5)

        # --- Botão de Extração ---
        self.extract_button = tk.Button(master, text="Extrair Códigos", command=self.start_extraction, font=('Arial', 12, 'bold'))
        self.extract_button.grid(row=2, column=0, columnspan=3, pady=20)

        # --- Área de Log/Resultados ---
        tk.Label(master, text="Resultados/Log:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.log_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=70, height=15, font=('Consolas', 10))
        self.log_text.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='nsew') # sticky para preencher o espaço

    def log_message(self, message, color="black"):
        """Adiciona uma mensagem na área de log."""
        self.log_text.insert(tk.END, message + "\n", color)
        self.log_text.see(tk.END) # Rola para o final
        self.master.update_idletasks() # Atualiza a GUI imediatamente

    def browse_pdf(self):
        """Abre a caixa de diálogo para selecionar o arquivo PDF."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os Arquivos", "*.*")]
        )
        if file_path:
            self.pdf_path_var.set(file_path)
            self.log_message(f"PDF selecionado: {file_path}")

    def browse_output_dir(self):
        """Abre a caixa de diálogo para selecionar a pasta de saída."""
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.output_dir_var.set(dir_path)
            self.log_message(f"Pasta de saída selecionada: {dir_path}")

    def start_extraction(self):
        """Inicia o processo de extração dos códigos."""
        self.log_text.delete(1.0, tk.END) # Limpa o log anterior
        pdf_path = self.pdf_path_var.get()
        output_dir = self.output_dir_var.get()

        if not pdf_path:
            self.log_message("Por favor, selecione o arquivo PDF.", "red")
            return
        if not os.path.exists(pdf_path):
            self.log_message(f"Erro: Arquivo PDF não encontrado em '{pdf_path}'", "red")
            return
        if not output_dir:
            self.log_message("Por favor, selecione a pasta para salvar os resultados.", "red")
            return
        if not os.path.isdir(output_dir):
            try:
                os.makedirs(output_dir) # Tenta criar a pasta se não existir
                self.log_message(f"Pasta de saída criada: {output_dir}", "blue")
            except OSError as e:
                self.log_message(f"Erro ao criar pasta de saída: {e}", "red")
                return

        self.log_message("Iniciando extração...", "blue")
        self.extract_button.config(state=tk.DISABLED) # Desabilita o botão durante o processo

        try:
            # 1. Extrair texto do PDF
            extracted_text = extract_text_from_pdf(pdf_path)
            self.log_message("Texto extraído do PDF. Analisando códigos...", "green")

            # 2. Encontrar códigos de produto
            product_codes = find_product_codes(extracted_text)

            # 3. Salvar os códigos em um arquivo
            if product_codes:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                output_filename = f"codigos_produtos_{timestamp}.txt"
                output_file_path = os.path.join(output_dir, output_filename)
                
                with open(output_file_path, "w", encoding="utf-8") as f:
                    for code in product_codes:
                        f.write(code + "\n")
                
                self.log_message(f"\n--- Extração Concluída! ---", "green")
                self.log_message(f"Total de códigos únicos encontrados: {len(product_codes)}", "green")
                self.log_message(f"Códigos salvos em: {output_file_path}", "green")
                
                # Exibe alguns códigos no log para visualização rápida
                self.log_message("\nPrimeiros 10 códigos (para visualização):", "blue")
                for i, code in enumerate(product_codes[:10]):
                    self.log_message(f"- {code}")
                if len(product_codes) > 10:
                    self.log_message("...")

            else:
                self.log_message("\nNenhum código de produto encontrado com os padrões especificados neste PDF.", "orange")

        except Exception as e:
            self.log_message(f"Ocorreu um erro durante a extração: {e}", "red")
        finally:
            self.extract_button.config(state=tk.NORMAL) # Reabilita o botão

# --- Iniciar a Aplicação ---
if __name__ == "__main__":
    # É importante instalar a biblioteca PyMuPDF (fitz) antes de rodar:
    # pip install PyMuPDF
    
    root = tk.Tk()
    app = ProductCodeExtractorApp(root)
    root.mainloop()
