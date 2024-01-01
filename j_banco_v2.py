import textwrap


def menu_v2():
   menu_v2= """\n
   ====================  MENU  ==================
   [d]\tDepositar
   [s]\tSacar
   [e]\tExtrato
   [nc]\tNova conta
   [lc]\tListar contas
   [nu]\tNovo usuário
   [t]\tSair
    => """
   return input(textwrap.dedent(menu_v2))


def depositar(saldo, valor, extrato, /):
   if valor >0:
      saldo += valor 
      extrato += f"Depósito:\tR$ {valor:.2f}\n"
      print("\n=== Depósito realizado com sucesso! ===")
   else:
      print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
   return saldo, extrato
   

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
   excedeu_saldo = valor > saldo
   excedeu_limite = valor > limite
   excedeu_saques = numero_saques >= limite_saques
   
   if excedeu_saldo: 
      print("\n@@@ Operaçaõ falhou! Você não tem saldo suficiente. @@@")
      
   elif excedeu_limite:
      print("\n@@@ Operação falhou! O valor do saue excede o limite. @@@ ")

   elif excedeu_saques:
      print("\n@@@ Operação falhou! Número máximo de saques excedidos. @@@")

   elif valor > 0 :
      saldo -= valor
      extrato += f"Saque:\tR$ {valor:.2f}\n"
      numero_saques += 1
      print("\n=== Saque realizado com sucesso!!! ===")

   else: 
      print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
   
   return saldo, extrato         


def exibir_extrato(saldo, /, *, extrato ):
   print("\n============= EXTRATO  ===============")
   print("Não foram realizadas movimentações." if not extrato else extrato)
   print(f"\nSaldo:\tR$ {saldo:.2f}")
   print("========================================")

   
def criar_usuario(usuarios):
   cpf = input("Infirme o seu CPF(somente números):")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:  #significa filto de usuário se ja retornou um usuário válido para o banco
      print("\n@@@ Já existe usuário com esse CPF! @@@")#se já existe um  usuário , retorna ao def main()
      return
   nome = input("Informe seu nome completo: ")#se não existe usuário, continua daqui
   data_nascemento = input("Informe a data de nascimento (dd-mm-aaaa):")
   endereco = input("Informe o endereço (logradouro, nro - bairro- cidade/sigla estado):")

   usuarios.append({"nome": nome, "data_nascimento": data_nascemento, "cpf": cpf, "endereco": endereco})#se tude for preenchido corretamente é criado um dicionário com essa estrutura de chave e valor

   print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]#Compressão de listas
   return usuarios_filtrados[0] if usuarios_filtrados else None #zero significa o retono  do primenro elemento


def criar_conta(agencia, numero_conta, usuarios):
   cpf = input("Informe o CPF do usuário: ")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario: #se encontrar o usuário continuar o codigo abaixo
      print("\n=== Conta criada com sucesso! ===")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}#estas chaves criam um dicionário
   
   print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
 

def listar_contas(contas):
   for conta in contas:
      linha = f"""\
           Agência:\t{conta['agencia']}
           C/C:\t{conta['numero_conta']}
           Titular:\t{conta['usuario']['nome']}
      """
      print("="* 100)
      print(textwrap.dedent(linha))


def main():
     LIMITES_SAQUES = 3
     AGENCIA = "0001"

     saldo = 0
     limite = 500
     extrato = ""
     numero_saques = 0
     usuarios = []
     contas = []
#numero_conta = 1
   
     while True:
       
      opcao = menu_v2() #informei o menú

      if opcao == "d":
         valor = float(input("Informe o valor do depósito: "))

         saldo, extrato = depositar(
            saldo,
            valor,
            extrato
            )
         

      elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITES_SAQUES,
          )
   
      elif opcao == "e":
       exibir_extrato(saldo, extrato=extrato)

      elif opcao == "nu":
       criar_usuario(usuarios)
 
      elif opcao == "nc":
          numero_conta = len(contas) + 1 #esta opção é válida, porem não finciona para excluir contas de usuários 
          conta = criar_conta(AGENCIA, numero_conta, usuarios)

          if conta:
            contas.append(conta)  #é colocado este append para não dar buges
        #numero_conta += 1   #esta opção é válida para excluir contas e está comentada no menu
       
      elif opcao == "lc":
       listar_contas(contas)

      elif opcao == "t" : 
        break

      else:
          print("Operção inválida ,  por favor selecione novamente a operação desejada. ")        


main()


#j_banco_v2="""
#[d]Depositar
#[s]Sacar
#[e]Extrato
#[t]Sair
#=>    """

#saldo=0
#limite=1000.00
#Extrato=""
#numero_saques=0
#LIMITES_SAQUES=3


#while True:
 #  opcao = input(j_banco_v2) 

   #if opcao == "d":
     #  valor = float(input("Informe o valor do depósito: "))

    #   if valor >0:
      #    saldo += valor
      #    Extrato += f"Deposito: R$ {valor:.2f}\n"
#
    #   else:
  #       print("Operação falhou! O valor informado é inválido.")   
    
#   elif opcao =="s":
   #   valor = float(input("Informe o valor de saque:"))
  #    excedeu_saldo = valor > saldo 
  #    excedeu_limite = valor > limite
  #    excedeu_saques= numero_saques >= LIMITES_SAQUES
        
  #    if excedeu_saldo:
   #      print("Operação falhou! Você não tem saldo suficiente. ")

   #   elif excedeu_limite:
     #    print("Operação falhou! O valor do saque excedeu o limite.") 

     # elif excedeu_saques: 
     #     print("Operação falhou! Número máximo de saques excedido.")   

    #  elif valor > 0:  
         
   #      saldo -= valor
         
      #   Extrato += f"Saque: R$ {valor:.2f}\n"   
         
     #    numero_saques += 1
    #  else:
    #     print("Operação falhou! O valor informado é inválido.")

      
      
   #elif opcao == "e":
  #    print("\n============= EXTRATO  ===============")
    #  print("Não foram realizadas movimentações." if not Extrato else Extrato)
    #  print(f"\nSaldo: R$ {saldo:.2f}")
    #  print("========================================")

#
   #elif opcao == "t":
  #    break

 #  else:
  #    print("Operação inválida, por favor selecionar novamente a operação desejada.")      

