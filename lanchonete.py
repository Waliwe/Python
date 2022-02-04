##original
import sys

print(20*"-"+ "Lanchonete" + 20*"-")
print("")

cardapio1 = []
lanches = {"pastel": 3.50, "coxinha": 4.50}
cardapio1.append(lanches)

cardapio2 = []
bebidas = {"coca lata": 3.50, "suco": 4.25}
cardapio2.append(bebidas)


while True:
        

        pedido = str(input("Qual o seu pedido?: Lanche ou Refri? ")) #Pedido
        if pedido == 'lanche':

            print("")
            print("Cardapio de lanches")
            print(16*"-")
            
            for lanche in cardapio1:
                for a, b in lanche.items():
                    print(a + ": "+str(b))
                print(16*"-")

                lanchep = str(input("Qual lanche voce quer "))
                if lanchep == "pastel":
                    print("Deu 3.50")
                if lanchep == "coxinha":
                    print("Deu 4.50") 
                    
        if pedido == 'refri':

            print("")
            print("Cardapio de lanches")
            print(16*"-")
            
            for bebida in cardapio2:
                for a, b in bebida.items():
                    print(a + ": "+str(b))
                print(16*"-")

                bebidap = str(input("Qual bebida voce quer "))
                if bebidap == "suco":
                    print("Deu 4.25")
                if bebidap == "coca lata":
                    print("Deu 3.50")
        break

