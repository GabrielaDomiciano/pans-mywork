# with open('workfile', 'r) as f
#       read_data = f.read()

#Function       Description
#read()           reads in data
#readline()       reads in line
#wite(data)        write data
#seek(offset)   move to a particular place in the file

# r  - open an existing file for reading
#r+  - open an existing filw for reading and writing
#a   - open file to appending
#w   - open/create a file for writeing (w+=write+read)
#x   - create a file(trows an error if the file exists already)

#    
#t  - -text mode(for text files)
#b  - binary mode (for binary files)

# messing with files 
# Author: Andrew Beatty

FILENAME= "data.txt"
'''
with open(FILENAME, 'rt') as f:
    for data in f:
        #print(data , end="" )
        print(data.strip() )
        #print(data[:-1])
'''
with open("data2.txt", "w+") as f:  
    f.write("what the hell\n")
    f.write("brown cow\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")
    
'''
with open("data2.txt", "w+") as f::
Aqui estamos abrindo um arquivo chamado "data2.txt" no modo de escrita e leitura ("w+"). O with é
 usado para garantir que o arquivo seja fechado 
corretamente após o uso. O arquivo é referenciado como f dentro do bloco with.

f.write("what the hell\n"):
Escreve a string "what the hell\n" no arquivo f.
f.write("brown cow\n"):
Escreve a string "brown cow\n" no arquivo f. \n é um caractere especial que representa uma nova linha.

f.seek(0):
Define a posição do cursor para o início do arquivo. Isso é feito para que possamos ler o conteúdo 
do arquivo a partir do início.
data = f.read():
Lê todo o conteúdo do arquivo f e armazena na variável data.
print(data):
Imprime o conteúdo do arquivo que foi lido.
print("done"):
Simplesmente imprime "done" após todas as operações serem concluídas.

Em resumo, este código abre um arquivo chamado "data2.txt", escreve duas linhas nele, 
lê o conteúdo das linhas escritas e o imprime 
na tela, e finalmente imprime "done" para indicar que todas as operações foram concluídas.

'''
