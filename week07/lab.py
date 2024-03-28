# Abre o arquivo
with open("moby_dick.txt", "r") as arquivo:
    # Lê todas as linhas do arquivo
    linhas = arquivo.readlines()

# Inicializa o contador de 'e's
Qt = 0

# Itera sobre cada linha do arquivo
for linha in linhas:
    # Itera sobre cada caractere da linha
    for letra in linha:
        # Converte a letra para minúscula antes de comparar
        if letra.lower() == "e":
            # Incrementa o contador de 'e's
            Qt += 1

# Imprime o resultado
print('No arquivo de texto "moby_dick.txt", existem', Qt, 'letras "E".')       




#moby_dick = 'Better to sleep with a sober cannibal than a drunk  eeeeChristian'
#Qt= 0
#for letter in moby_dick : 
 #   if letter.lower() == 'e':
 #       Qt = Qt + 1
#print('in the text file', moby_dick, 'there are', Qt, 'letters E')


