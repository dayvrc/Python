USUARIO_MASTER = {"usuario": "dev", "senha": "master"}

def pedir_login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    return usuario, senha

def main():
    while True:
        usuario, senha = pedir_login()
        
        if usuario == USUARIO_MASTER["usuario"] and senha == USUARIO_MASTER["senha"]:
            print("Acesso master concedido!")
            break
        elif usuario == "user" and senha == "senha123":
            print("Acesso usuário concedido!")
            break
        else:
            print("Usuário ou senha incorretos!")

if __name__ == "__main__":
    main()
