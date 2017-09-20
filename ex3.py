print(" ======= CADASTRO DE Nomes ======== \n")
i = 0
lista = []
while (i<3):
  lista.append(input("Digite um nome: " ))
  i+=1
lista.reverse()
print ("======== Nomes em ordem inversa ========= ")

for i in range(len(lista)):
  print(lista[i])
  i+=1