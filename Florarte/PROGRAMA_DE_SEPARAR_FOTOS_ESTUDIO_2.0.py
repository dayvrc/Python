import os
import shutil
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox, scrolledtext
import fitz  # PyMuPDF para PDF
from docx import Document  # python-docx para DOCX
import re  # Expressões regulares

# --- FUNÇÕES DE EXTRAÇÃO DE TEXTO ---

def _extract_text_from_pdf(pdf_path):
    text = ""
    try:
        document = fitz.open(pdf_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text() + "\n"
        document.close()
    except Exception as e:
        raise Exception(f"Erro ao extrair texto do PDF: {e}")
    return text

def _extract_text_from_docx(docx_path):
    text = ""
    try:
        doc = Document(docx_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        raise Exception(f"Erro ao extrair texto do DOCX: {e}")
    return text

def _extract_text_from_txt(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        try:
            with open(txt_path, 'r', encoding='iso-8859-1') as f:
                text = f.read()
        except Exception as e_alt:
            raise Exception(f"Erro ao extrair texto do TXT: {e_alt}")
    return text

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return _extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return _extract_text_from_docx(file_path)
    elif ext == '.txt':
        return _extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Tipo de arquivo não suportado: {ext}. Use .pdf, .docx ou .txt.")

def find_product_codes(text_content):
    """
    Encontra códigos de produto no texto extraído:
    - 6 dígitos
    - 8 dígitos
    - 8 dígitos + F
    - Qualquer um desses seguidos de _n (ex: 123456_1, 12345678_2, 12345678F_3)
    """
    regex_pattern = (
        r'\b\d{8}F_\d+\b|'      # 8 dígitos + F + _n
        r'\b\d{8}_\d+\b|'       # 8 dígitos + _n
        r'\b\d{6}_\d+\b|'       # 6 dígitos + _n
        r'\b\d{8}F\b|'          # 8 dígitos + F
        r'\b\d{8}\b|'           # 8 dígitos
        r'\b\d{6}\b'            # 6 dígitos
    )
    found_codes = re.findall(regex_pattern, text_content)
    return sorted(list(set(found_codes)))

# --- FUNÇÕES DE INTERFACE E LÓGICA ---

def copiar_fotos(origem, destino, nomes_arquivos):
    erros = []
    for nome_arquivo in nomes_arquivos:
        nome_arquivo = nome_arquivo.strip()
        if not nome_arquivo.lower().endswith('.jpg'):
            nome_arquivo += '.jpg'
        caminho_origem = os.path.join(origem, nome_arquivo)
        caminho_destino = os.path.join(destino, nome_arquivo)
        try:
            shutil.copy2(caminho_origem, caminho_destino)
        except FileNotFoundError:
            erros.append(nome_arquivo)
        except Exception as e:
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

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo com os códigos dos produtos",
        filetypes=[
            ("Arquivos de Documento", "*.pdf *.docx *.txt"),
            ("Arquivos PDF", "*.pdf"),
            ("Arquivos Word (DOCX)", "*.docx"),
            ("Arquivos de Texto (TXT)", "*.txt"),
            ("Todos os Arquivos", "*.*")
        ]
    )
    if caminho:
        entrada_txt.delete(0, END)
        entrada_txt.insert(0, caminho)

def exportar_log():
    conteudo = log_text.get("1.0", "end").strip()
    if not conteudo:
        messagebox.showinfo("Exportação de Log", "O log está vazio.")
        return
    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")],
        title="Salvar log como..."
    )
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        messagebox.showinfo("Exportação de Log", f"Log exportado para:\n{caminho}")

def iniciar_copia():
    origem = entrada_origem.get()
    destino = entrada_destino.get()
    arquivo_com_codigos = entrada_txt.get()
    log_text.delete("1.0", "end")

    if not (origem and destino and arquivo_com_codigos):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos antes de iniciar.")
        log_text.insert("end", "ERRO: Campos obrigatórios não preenchidos.\n")
        return

    if not os.path.exists(arquivo_com_codigos):
        messagebox.showerror("Erro", "Arquivo selecionado não encontrado.")
        log_text.insert("end", f"ERRO: Arquivo não encontrado: {arquivo_com_codigos}\n")
        return

    try:
        texto_extraido = extract_text_from_file(arquivo_com_codigos)
        nomes_para_copiar = find_product_codes(texto_extraido)
        if not nomes_para_copiar:
            msg = "Nenhum código de produto foi encontrado no arquivo selecionado."
            messagebox.showinfo("Nenhum Código Encontrado", msg)
            log_text.insert("end", "AVISO: Nenhum código encontrado.\n")
            return
    except ValueError as ve:
        messagebox.showerror("Erro no Tipo de Arquivo", str(ve))
        log_text.insert("end", f"ERRO: {ve}\n")
        return
    except Exception as e:
        messagebox.showerror("Erro na Extração de Códigos", f"Ocorreu um erro ao extrair os códigos do arquivo: {e}")
        log_text.insert("end", f"ERRO: {e}\n")
        return

    log_text.insert("end", f"Total de códigos encontrados: {len(nomes_para_copiar)}\n")
    log_text.insert("end", "Iniciando cópia dos arquivos...\n")

    erros = copiar_fotos(origem, destino, nomes_para_copiar)

    for nome in nomes_para_copiar:
        nome_jpg = nome if nome.lower().endswith('.jpg') else nome + ".jpg"
        if nome_jpg in erros or any(nome in erro for erro in erros):
            log_text.insert("end", f"FALHA: {nome_jpg} não encontrado ou erro na cópia.\n")
        else:
            log_text.insert("end", f"OK: {nome_jpg} copiado.\n")

    if erros:
        messagebox.showwarning("Concluído com erros", f"{len(erros)} arquivos não encontrados ou com erro na cópia:\n" + "\n".join(erros))
        log_text.insert("end", f"\nConcluído com erros: {len(erros)} arquivos não encontrados ou erro na cópia.\n")
    else:
        messagebox.showinfo("Sucesso", f"Todos os {len(nomes_para_copiar)} arquivos foram copiados com sucesso!")
        log_text.insert("end", "\nSucesso: Todos os arquivos foram copiados.\n")

# --- INTERFACE GRÁFICA MODERNA ---

janela = tb.Window(themename="flatly")
janela.title("SAF 2.0 - Separador Automático de Fotos")
janela.geometry("500x500")
janela.resizable(False, False)

tb.Label(janela, text="Selecione a pasta onde estão as fotos:", bootstyle=PRIMARY).pack(pady=(10, 0))
entrada_origem = tb.Entry(janela, width=60)
entrada_origem.pack()
tb.Button(janela, text="Selecionar pasta", command=selecionar_origem, bootstyle=INFO).pack(pady=(10, 5))

tb.Label(janela, text="Selecione a pasta onde colocar as fotos separadas:", bootstyle=PRIMARY).pack()
entrada_destino = tb.Entry(janela, width=60)
entrada_destino.pack()
tb.Button(janela, text="Selecionar pasta", command=selecionar_destino, bootstyle=INFO).pack(pady=(10, 5))

tb.Label(janela, text="Selecione o arquivo de documento com os códigos dos produtos:", bootstyle=PRIMARY).pack()
entrada_txt = tb.Entry(janela, width=60)
entrada_txt.pack()
tb.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo, bootstyle=INFO).pack(pady=(10, 5))

tb.Button(janela, text="Iniciar cópia", command=iniciar_copia, bootstyle=SUCCESS, width=20).pack(pady=10)

frame_log = tb.Frame(janela)
frame_log.pack(pady=(5, 10), fill="both", expand=False)
tb.Label(frame_log, text="Log de execução:", bootstyle=PRIMARY).pack(anchor="w")
log_text = scrolledtext.ScrolledText(frame_log, width=60, height=10, font=("Consolas", 10))
log_text.pack(side="left", fill="both", expand=True)
btn_exportar_log = tb.Button(frame_log, text="Exportar log", command=exportar_log, bootstyle=SECONDARY)
btn_exportar_log.pack(side="right", padx=5, pady=5)

janela.mainloop()