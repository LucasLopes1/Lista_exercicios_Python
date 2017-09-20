print (" Taboada ")
cont = 0
numero = int(input("Digite o Numero a ser cauculado:  "))
print ("Taboada do numero: ",numero)
if 1<=numero<=10:
  while cont<=10:
    print (numero," X ", cont," = ", cont*numero )
    cont+=1
    
else:
  print ("Digite um numero entre 1 e 10 ")