import os
import shutil
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox

# --- NOVAS IMPORTAÇÕES PARA EXTRAÇÃO DE TEXTO ---
import fitz  # Para PDF (PyMuPDF)
from docx import Document # Para DOCX (python-docx)
import re    # Para expressões regulares
# --- FIM NOVAS IMPORTAÇÕES ---


# --- FUNÇÕES DE LÓGICA DE EXTRAÇÃO DE TEXTO (Integradas do script anterior) ---

def _extract_text_from_pdf(pdf_path):
    """Extrai todo o conteúdo de texto de um arquivo PDF."""
    text = ""
    try:
        document = fitz.open(pdf_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text() + "\n" # Adiciona quebra de linha entre páginas
        document.close()
    except Exception as e:
        raise Exception(f"Erro ao extrair texto do PDF: {e}")
    return text

def _extract_text_from_docx(docx_path):
    """Extrai todo o conteúdo de texto de um arquivo DOCX."""
    text = ""
    try:
        doc = Document(docx_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        raise Exception(f"Erro ao extrair texto do DOCX: {e}")
    return text

def _extract_text_from_txt(txt_path):
    """Extrai todo o conteúdo de texto de um arquivo TXT."""
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        # Tenta com encoding ISO-8859-1 se UTF-8 falhar
        try:
            with open(txt_path, 'r', encoding='iso-8859-1') as f:
                text = f.read()
        except Exception as e_alt:
            raise Exception(f"Erro ao extrair texto do TXT (UTF-8 ou ISO-8859-1): {e_alt}")
    return text

def extract_text_from_file(file_path):
    """
    Função universal para extrair texto de PDF, DOCX ou TXT.
    Determina o tipo do arquivo pela extensão.
    """
    file_extension = os.path.splitext(file_path)[1].lower() # Pega a extensão e converte para minúsculas

    if file_extension == '.pdf':
        return _extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        return _extract_text_from_docx(file_path)
    elif file_extension == '.txt':
        return _extract_text_from_txt(file_path)
    else:
        # Levanta um erro se o tipo de arquivo não for suportado
        raise ValueError(f"Tipo de arquivo não suportado: {file_extension}. Por favor, selecione um arquivo .pdf, .docx ou .txt.")

def find_product_codes(text_content):
    """
    Encontra códigos de produto no texto extraído com base em padrões específicos:
    - Exatamente 6 dígitos numéricos
    - Exatamente 8 dígitos numéricos
    - Exatamente 8 dígitos numéricos seguidos pela letra 'F' (total de 9 caracteres)
    """
    # Ordem das alternativas é importante: padrões mais específicos/longos primeiro.
    regex_pattern = r'\b\d{8}F\b|\b\d{8}\b|\b\d{6}\b'
    
    found_codes = re.findall(regex_pattern, text_content)
    
    # Remove duplicatas e ordena
    return sorted(list(set(found_codes)))

# --- FIM FUNÇÕES DE LÓGICA DE EXTRAÇÃO DE TEXTO ---


# --- FUNÇÕES EXISTENTES DO SEU CÓDIGO ---

def copiar_fotos(origem, destino, nomes_arquivos):
    erros = []
    for nome_arquivo in nomes_arquivos:
        nome_arquivo = nome_arquivo.strip()
        # Adiciona .jpg apenas se não for uma extensão de arquivo válida já (como .png, se você expandir no futuro)
        # Por enquanto, mantemos .jpg para garantir.
        if not nome_arquivo.lower().endswith('.jpg'):
            nome_arquivo += '.jpg'

        caminho_origem = os.path.join(origem, nome_arquivo)
        caminho_destino = os.path.join(destino, nome_arquivo)

        try:
            shutil.copy2(caminho_origem, caminho_destino)
        except FileNotFoundError:
            erros.append(nome_arquivo)
        except Exception as e: # Captura outros erros de cópia
            erros.append(f"{nome_arquivo} (Erro: {e})")

    return erros

def selecionar_origem():
    caminho = filedialog.askdirectory(title="Selecione a pasta onde estão as fotos")
    if caminho:
        entrada_origem.delete(0, END)
        entrada_origem.insert(0, caminho)

def selecionar_destino():
    caminho = filedialog.askdirectory(title="Selecione a pasta onde colocar as fotos separadas")
    if caminho:
        entrada_destino.delete(0, END)
        entrada_destino.insert(0, caminho)

# --- FUNÇÃO `selecionar_arquivo` MODIFICADA ---
def selecionar_arquivo():
    # Agora aceita .pdf, .docx e .txt
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo com os códigos dos produtos",
        filetypes=[
            ("Arquivos de Documento", "*.pdf *.docx *.txt"), # Agrupa todos os tipos
            ("Arquivos PDF", "*.pdf"),
            ("Arquivos Word (DOCX)", "*.docx"),
            ("Arquivos de Texto (TXT)", "*.txt"),
            ("Todos os Arquivos", "*.*")
        ]
    )
    if caminho:
        entrada_txt.delete(0, END) # O nome da Entry ainda é 'entrada_txt', mas agora aceita outros tipos
        entrada_txt.insert(0, caminho)
        # Opcional: Atualizar um Label ou exibir uma mensagem no status bar
        # para indicar que o arquivo foi selecionado.

# --- FUNÇÃO `iniciar_copia` MODIFICADA ---
def iniciar_copia():
    origem = entrada_origem.get()
    destino = entrada_destino.get()
    arquivo_com_codigos = entrada_txt.get() # Renomeado para clareza, mas é o mesmo Entry

    if not (origem and destino and arquivo_com_codigos):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos antes de iniciar.")
        return

    if not os.path.exists(arquivo_com_codigos):
        messagebox.showerror("Erro", "Arquivo selecionado não encontrado.")
        return

    # --- NOVA LÓGICA DE EXTRAÇÃO E PROCESSAMENTO DOS NOMES ---
    try:
        # 1. Extrair o texto do arquivo selecionado
        texto_extraido = extract_text_from_file(arquivo_com_codigos)
        
        # 2. Encontrar os códigos de produto no texto
        nomes_para_copiar = find_product_codes(texto_extraido)

        if not nomes_para_copiar:
            messagebox.showinfo("Nenhum Código Encontrado", 
                                "Nenhum código de produto foi encontrado no arquivo selecionado "
                                "com os padrões especificados (6, 8, ou 9 dígitos com 'F' no final).")
            return

    except ValueError as ve:
        messagebox.showerror("Erro no Tipo de Arquivo", str(ve))
        return
    except Exception as e:
        messagebox.showerror("Erro na Extração de Códigos", 
                            f"Ocorreu um erro ao extrair os códigos do arquivo: {e}")
        return
    # --- FIM NOVA LÓGICA ---

    erros = copiar_fotos(origem, destino, nomes_para_copiar) # Passa os códigos encontrados

    if erros:
        messagebox.showwarning("Concluído com erros", f"{len(erros)} arquivos não encontrados ou com erro na cópia:\n" + "\n".join(erros))
    else:
        messagebox.showinfo("Sucesso", f"Todos os {len(nomes_para_copiar)} arquivos foram copiados com sucesso!")

# ----- INTERFACE GRÁFICA MODERNA -----
janela = tb.Window(themename="flatly")
janela.title("SAF - Separador Automatico de Fotos")
janela.geometry("500x400") # Aumentei um pouco a altura para acomodar mensagens
janela.resizable(False, False)

# Caminho origem
tb.Label(janela, text="Selecione a pasta onde estão as fotos:", bootstyle=PRIMARY).pack(pady=(10, 0))
entrada_origem = tb.Entry(janela, width=60)
entrada_origem.pack()
tb.Button(janela, text="Selecionar pasta", command=selecionar_origem, bootstyle=INFO).pack(pady=(10, 5))

# Caminho destino
tb.Label(janela, text="Selecione a pasta onde colocar as fotos separadas:", bootstyle=PRIMARY).pack()
entrada_destino = tb.Entry(janela, width=60)
entrada_destino.pack()
tb.Button(janela, text="Selecionar pasta", command=selecionar_destino, bootstyle=INFO).pack(pady=(10, 5))

# Arquivo de códigos (agora pode ser PDF, DOCX, TXT)
tb.Label(janela, text="Selecione o arquivo de documento com os códigos dos produtos:", bootstyle=PRIMARY).pack()
entrada_txt = tb.Entry(janela, width=60)
entrada_txt.pack()
tb.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo, bootstyle=INFO).pack(pady=(10, 5))

# Botão de iniciar
tb.Button(janela, text="Iniciar cópia", command=iniciar_copia, bootstyle=SUCCESS, width=20).pack(pady=10)

janela.mainloop()
