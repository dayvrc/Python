import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import hashlib

# Conexão com o banco
def conectar_db():
    conn = sqlite3.connect("notas.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            senha TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

# Função para hash da senha
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Interface de login
class TelaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Login - Cofre de Notas")
        self.master.geometry("350x200")
        self.master.resizable(False, False)

        self.label = ttk.Label(master, text="Digite sua senha:")
        self.label.pack(pady=10)

        self.senha_entry = ttk.Entry(master, show="*")
        self.senha_entry.pack(pady=5)

        self.botao_login = ttk.Button(master, text="Entrar", command=self.verificar_login)
        self.botao_login.pack(pady=15)

        self.status_label = ttk.Label(master, text="")
        self.status_label.pack()

        # Checa se existe uma senha cadastrada
        self.conn = conectar_db()
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM usuarios")
        resultado = self.cursor.fetchone()

        if resultado is None:
            self.label.config(text="Crie sua senha mestre:")
            self.novo_usuario = True
        else:
            self.novo_usuario = False

    def verificar_login(self):
        senha = self.senha_entry.get()
        senha_hash = hash_senha(senha)

        if self.novo_usuario:
            self.cursor.execute("INSERT INTO usuarios (senha) VALUES (?)", (senha_hash,))
            self.conn.commit()
            messagebox.showinfo("Cadastro", "Senha cadastrada com sucesso!")
            self.master.destroy()
            abrir_tela_notas()
        else:
            self.cursor.execute("SELECT senha FROM usuarios")
            senha_salva = self.cursor.fetchone()[0]
            if senha_hash == senha_salva:
                self.master.destroy()
                abrir_tela_notas()
            else:
                self.status_label.config(text="Senha incorreta!", foreground="red")

# Interface principal de notas
class TelaNotas:
    def __init__(self, master):
        self.master = master
        self.master.title("Cofre de Notas")
        self.master.geometry("600x400")

        self.conn = conectar_db()
        self.cursor = self.conn.cursor()

        # Layout
        self.frame_esquerda = ttk.Frame(master)
        self.frame_esquerda.pack(side="left", fill="y", padx=10, pady=10)

        self.frame_direita = ttk.Frame(master)
        self.frame_direita.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.lista_notas = tk.Listbox(self.frame_esquerda)
        self.lista_notas.pack(fill="y")
        self.lista_notas.bind('<<ListboxSelect>>', self.carregar_nota)

        self.botao_nova = ttk.Button(self.frame_esquerda, text="Nova Nota", command=self.nova_nota)
        self.botao_nova.pack(pady=5)

        self.titulo_entry = ttk.Entry(self.frame_direita)
        self.titulo_entry.pack(fill="x", pady=5)

        self.texto = tk.Text(self.frame_direita)
        self.texto.pack(expand=True, fill="both")

        self.botao_salvar = ttk.Button(self.frame_direita, text="Salvar Nota", command=self.salvar_nota)
        self.botao_salvar.pack(pady=5)

        self.id_nota_atual = None
        self.carregar_lista_notas()

    def carregar_lista_notas(self):
        self.lista_notas.delete(0, tk.END)
        self.cursor.execute("SELECT id, titulo FROM notas")
        for nota in self.cursor.fetchall():
            self.lista_notas.insert(tk.END, f"{nota[0]} - {nota[1]}")

    def carregar_nota(self, event):
        if not self.lista_notas.curselection():
            return
        index = self.lista_notas.curselection()[0]
        nota_id = int(self.lista_notas.get(index).split(" - ")[0])

        self.cursor.execute("SELECT titulo, conteudo FROM notas WHERE id=?", (nota_id,))
        nota = self.cursor.fetchone()
        if nota:
            self.id_nota_atual = nota_id
            self.titulo_entry.delete(0, tk.END)
            self.titulo_entry.insert(0, nota[0])
            self.texto.delete("1.0", tk.END)
            self.texto.insert("1.0", nota[1])

    def nova_nota(self):
        self.id_nota_atual = None
        self.titulo_entry.delete(0, tk.END)
        self.texto.delete("1.0", tk.END)

    def salvar_nota(self):
        titulo = self.titulo_entry.get()
        conteudo = self.texto.get("1.0", tk.END).strip()
        if not titulo or not conteudo:
            messagebox.showwarning("Campos vazios", "Preencha o título e o conteúdo!")
            return
        if self.id_nota_atual:
            self.cursor.execute("UPDATE notas SET titulo=?, conteudo=? WHERE id=?",
                                (titulo, conteudo, self.id_nota_atual))
        else:
            self.cursor.execute("INSERT INTO notas (titulo, conteudo) VALUES (?, ?)", (titulo, conteudo))
        self.conn.commit()
        self.carregar_lista_notas()
        messagebox.showinfo("Sucesso", "Nota salva com sucesso!")

# Início
def abrir_tela_notas():
    root = tk.Tk()
    app = TelaNotas(root)
    root.mainloop()

def main():
    login_root = tk.Tk()
    login_app = TelaLogin(login_root)
    login_root.mainloop()

if __name__ == "__main__":
    main()
