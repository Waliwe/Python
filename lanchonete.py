##teste
import sys

print(20*"-"+ "Lanchonete" + 20*"-")
print("")

cardapio1 = []
lanches = {"pastel": 3.50, "coxinha": 4.50}
cardapio1.append(lanches)

cardapio2 = []
bebidas = {"suco": 4.25,"coca lata": 3.50}
cardapio2.append(bebidas)

produtos = []
quantidade = []


while True:
        

        pedido = str(input("Qual o seu pedido?: Lanche ou bebida? ")) #Pedido
        if pedido == 'lanche':

            print("")
            print("Cardapio de lanches")
            print(16*"-")
            
            for lanche in cardapio1:
                for a, b in lanche.items():
                    print(a + ": "+str(b))
                print(16*"-")

                lanchep = str(input("Qual lanche voce quer ?: "))
                produtos.append(lanchep)
                if lanchep == "pastel":
                        y=int(input('qual a quantidade?'))
                        quantidade.append(y)
                        
                        cont=str(input('Gostaria de continuar suas compras?: [S/N]')).upper()
    
                        if cont == 'N':
                            print(f'Seu pedido foi {y} {lanchep} no valor de: {lanches["pastel"]*y}')
        break
                        
                             

                    
        if pedido == 'bebida':

            print("")
            print("Cardapio de bebidas")
            print(16*"-")
            
            for bebida in cardapio2:
                for a, b in bebida.items():
                    print(a + ": "+str(b))
                print(16*"-")

                bebidap = str(input("Qual bebida voce quer ?: "))
                if bebidap == "suco":
                        y=int(input('qual a quantidade?'))
                        print(f'Seu pedido foi {y} {bebidap} no valor de: {bebidas["suco"]*y}')
                        

