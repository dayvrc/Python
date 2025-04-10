from tkinter import * 

root = Tk()
root.title("Exibir Imagem")
root.minsize(200,400)
root.geometry("300x300")

text = Label(root, text="Nome")
text.pack()
text2 = Label(root, text="Nome2")
text.pack()

image = PhotoImage(file=r"C:\Users\dayvs\Documents\Repositorios_vscode\Python\Estacio\RAD\green_lantern.png")
img = Label(root, image=image)
img.pack()

root.mainloop()