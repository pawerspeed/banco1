banco1="""
[d]Depositar
[s]Sacar
[e]Extrato
[t]Sair
=>    """

saldo=0
limite=500
Extrato=""
numero_saques=0
limite_SAQUES=3


while True:

   opcao = input(banco1)

   if opcao == "d":
      
      valor = float(input("Informe o valor do depósito: "))

      if valor >0:
         
         saldo += valor

         Extrato += f"Deposito: R$ {valor:.2f}\n"

      else:
        print("Operação falhou! O valor informado é inválido.")   
     
   elif opcao =="s":
      valor = float(input("Informe o valor de saque:"))

      excedeu_saldo = valor > saldo 

      excedeu_limite = valor > limite

      excedeu_saques= numero_saques >= limite_SAQUES

      if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente. ")

      elif excedeu_limite:
         print("Operação falhou! O valor do saque excedeu o limite.") 

      elif excedeu_saques: 
          print("Operação falhou! Número máximo de saques excedido.")   

      elif valor > 0:  
         
         saldo -= valor
         
         Extrato += f"Saque: R$ {valor:.2f}\n"   
         
         numero_saques += 1
      else:
         print("Operação falhou! O valor informado é inválido.")

      
      
   elif opcao == "e":
      
      print("\n============= EXTRATO  ===============")
      
      print("Não foram realizadas movimentações." if not Extrato else Extrato)
      
      print(f"\nSaldo: R$ {saldo:.2f}")

      print("=========================================")


   elif opcao == "t":
      break

   else:
      print("Operação inválida, por favor selecionar novamente a operação desejada.")      
