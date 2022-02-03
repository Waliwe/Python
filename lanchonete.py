
import sys

print("Lanchonete")

cardapio1 = []
lanches = {"pastel": 3.50, "coxinha": 4.50}
cardapio1.append(lanches)

cardapio2 = []
bebidas = {"coca lata": 3.50, "suco": 4.25}
cardapio2.append(bebidas)

quantidade = []
carrinho = []
total = []
while True:
    try:
        

        pedido = str(input("Qual o seu pedido?: Lanche ou Refri? ")) #Pedido
        if pedido == 'lanche':

            print("")
            print("Cardapio de lanches")
            print(16*"-")
            
            for lanche in cardapio1:
                for a, b in lanche.items():
                    print(a + ": "+str(b))
                print(16*"-")



                lan = str(input("Escolha um lanche: "))
                carrinho.append(lan)
                if lan == ("pastel"):
                        quanti=int(input("Quantos pasteis são? "))
                        quantidade.append(quanti)
                
                pagar = quanti * 3.50
                ##print(pagar)
                total.append(pagar)
                pagar_total=sum(total)
    except:
        print('error')