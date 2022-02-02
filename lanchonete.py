import sys

print("Lanchonete")

cardapio1 = []
lanches = {"pastel": 3.50, "coxinha": 4.50}
cardapio1.append(lanches)

cardapio2 = []
bebidas = {"coca lata": 3.50, "suco": 4.25}
cardapio2.append(bebidas)


while True:
    pedido = str(input("Qual o seu pedido? ('lanche', 'refri')"))
    if pedido == 'lanche':
        print("lanches")
        print(16*"-")
        for lanche in cardapio1:
            for a, b in lanche.items():
                print(a + ": "+str(b))
    lan = str(input("Escolha um lanche: "))
    if lan == ("pastel"):
        print("s")
    if lan == ("coxinha"):
        print("ss")

    if pedido == 'refri':
        print('bebidas')
        print(16*"-")
        for bebida in cardapio2:
            for x, y in bebida.items():
                print(x + ": "+str(y))
    beb = str(input("Escolha uma bebida: "))
    if beb == ("coca lata"):
        print("s")
    if beb == ("suco"):
        print("ss")
