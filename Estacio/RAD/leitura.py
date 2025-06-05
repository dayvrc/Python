with open(r"estacio\rad\texto.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write('\nescrevendo no arquivo\n')
    arquivo.write('escrevendo óóo arquivo2\n')

with open(r"estacio\rad\texto.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
print(conteudo)

with open()