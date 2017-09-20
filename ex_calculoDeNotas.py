op = 1
lista = []
cont = 0
sete =0
print(" ======= CADASTRO DE NOTAS ======== \n")
while (op ==1):
  lista.append(float (input("Digite a Nota: " )))
  op = int (input("Deseja Cadastrar Outra ? 1- SIM ou -1 NAO :"))
  print("\n")
print("=== Quantidade de Valores Lidos === \n%d" %len(lista))
print("\n ==== Valores Lidos em Ordem que foram Informados ====")
for i in range(len(lista)):
  print('%0.2f'%lista[i])
print("\n ==== Valores Lidos em Ordem Inversa ====")
lista.reverse()
for i in range(len(lista)):
  print('%0.2f'%lista[i])
print("\n ==== A soma dos valores lidos ====")
print (sum(lista))
print("\n ==== A Media dos valores lidos ====")
media = sum(lista)/len(lista)
print ('%0.2f'%media)
for j in range(len(lista)):
  if (lista[j] > media):
    cont = cont + 1
    if (lista[j] < 7):
      sete =sete + 1
print("\n ==== Quantidade de Valores acima da Media ==== \n %d"%cont)
print("\n ==== Quantidade de Valores abaixo de 7 ==== \n %d"%sete)
print("\n ============== FIM DO PROGRAMA ============= \n")