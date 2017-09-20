print ("verificando a relação com a vitima.")
cont=0
pergunta = int(input("Telefonou para a vitima? SIM[1] NÃO[2]\n"))
if pergunta == 1:
  cont=cont+1

pergunta = int(input("Esteve no local do crime? SIM[1] NÃO[2]\n"))  
if pergunta == 1:
  cont=cont+1
  
pergunta = int(input("Mora perto da vitima? SIM[1] NÃO[2]\n"))  
if pergunta == 1:
  cont=cont+1  

pergunta = int(input("Devia para a vitima? SIM[1] NÃO[2]\n"))  
if pergunta == 1:
  cont=cont+1

pergunta = int(input("Ja trabalhou com a vitima? SIM[1] NÃO[2\n]"))  
if pergunta == 1:
  cont=cont+1  
  
if cont<=1:
  print("Inocente!")
elif cont==2:
  print("Suspeito!")
elif 3<=cont<=4:
  print("Cumplice!")
else:
  print("Assassino")