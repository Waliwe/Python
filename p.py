cardapio = {"coca": 4, "pastel": 6}

for x in cardapio:
    for a, b in cardapio.items():
        print(a + ": "+str(b))

x= input("escolha o seu pedido: ")
y= int(input("Qual a quantidade? "))

print(f"su pedido foi {y} {x} no valor de {cardapio[x]*y} reais")

