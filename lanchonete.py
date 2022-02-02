## lanchonete.test
import sys

print("Lanchonete")

cardapio1 = []
lanches = {"pastel": 3.50, "coxinha": 4.50}
cardapio1.append(lanches)

cardapio2 = []
bebidas = {"coca lata": 3.50, "suco": 4.25}
cardapio2.append(bebidas)
1
quantidade = []
listSum = sum(quantidade)

while True:
    try:
        pedido = str(input("Qual o seu pedido? ('lanche', 'refri')"))
        if pedido == 'lanche':
            print("lanches")
            print(16*"-")
            for lanche in cardapio1:
                for a, b in lanche.items():
                    print(a + ": "+str(b))
                lan = str(input("Escolha um lanche: "))
                if lan == ("pastel"):
                        quanti=str(input("Quantos pasteis são?"))
                        quantidade.append(quanti)

                if lan == ("coxinha"):
                        quanti2=str(input("Quantas coxinhas são?"))
                        quantidade.append(quanti2)
                        print(quanti2)
        
        n_s = str(input('Dejesa comprar algo mais? (s)-(n): ')).upper()
        if n_s == 'n':
            break       

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

        s_n = str(input('Dejesa comprar algo mais? (s)-(n): ')).upper()
        if s_n == 'n':
            break
    except:
        print('error')