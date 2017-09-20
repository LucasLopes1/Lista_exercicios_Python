import os
listaNome = []
listaEmail = []
listaRmal = []
listaPagamentos = []
listaCotas = []
listaDevendo = []
listaNumeros = []
quantCotas = 0
tipoSena = 0
data = 0
numSorteio = 0
valorCota = 0
contCotas = 0

# funão que solicita nomes, emails, Ramais, numero de cotas, dezenas e confirma o pagamento
def FichaApostador():
  listaNome.append(input("Digite o nome: "))
  listaEmail.append(input("Digite o email: "))
  listaRmal.append(input("Digite o ramal: "))
  numeros = int(input("Quantas Cotas Jogadas?: "))
  listaCotas.append(numeros)
  i=0
  while i < numeros:
    listaNumeros.append(input("Digite as dezenas separadas por virgula: "))
    i=i+1
  listaPagamentos.append(int(input("Realizou pagamento? sim[1] não[2]: ")))

  return
#Solicita Informaçoes do Sorteio
def cota():
  global valorCota
  global quantCotas
  global tipoSena
  global data
  global numSorteio
  valorCota = input("valor da cota: ")
  quantCotas= int(input("Quantidades de Cotas: "))
  tipoSena = input("Qual modalidade: ")
  data= input("digite a data do Sorteio: ")
  numSorteio = int(input("digite o Numero do sorteio: "))
  return 
#fasz a busca pela lista de pagamentos e sempre que encontar o Numero 2, pega o nome de mesmo indice na lista de nomes e insere na lista de devedores
def devendo():
  i = 0
  while i < len(listaPagamentos):
    if listaPagamentos[i] == 2:
      listaDevendo.append(listaNome[i])
      i = i+1
    else:
      i= i+1
  print("Nome de quem falta Pagar: ",listaDevendo)  
  return 

# soma as cotas da listaCotas e subitari da vaiavel quantCotas(inserida pelo usuario)
def cotasDisponiveis():
  global quantCotas
  global contCotas
  i = 0
  
  while i< len(listaNome):
    contCotas = contCotas+listaCotas[i]
    i = i+1
  print("total de cotas: ",quantCotas,"\n total de cotas já adiquiridas: ", contCotas," \n Cotas dispiniveis: ", (quantCotas-contCotas))  


#mostra todos os Participantes, as dezenas apostadas, valor por aposta, quntidade de cotas apostadas tipo de sorteio, o numero do sorteio  
def relatorio():
  print ("=======Participantes=======")
  print (listaNome)
  print ("\n=========Numeros============")
  print(listaNumeros)
  print ("\n=========sorteio============")
  global valorCota
  global quantCotas
  global tipoSena
  global data
  global numSorteio
  global contCotas
  
  print ("\n Valor por cota: ",valorCota,"\n total de cotas apostadas: ", contCotas,"\n sorteio em: ",data," \n sorteio de NUmero: ", numSorteio)
  
  return   
  
  
  
     
    
  
print ("==========Bolão=============")
while True:
  x = int(input("\n \n Escolha uma opção: Apostadores[1], Sorteio[2], Devedores[3], Verificar Cotas[4], Relatorio[5], Limpar[0]: \n"))
  
  if x == 1:
      FichaApostador()
  elif x==2:
       cota()
  elif x==3:
      devendo()
  elif x == 4:
      cotasDisponiveis()
  elif x == 5:
      relatorio()
  elif x== 0:
    os.system('clear')