          
                if lan == ("coxinha"):
                        quanti2=str(input("Quantas coxinhas são?"))
                        quantidade.append(quanti2)
                        print(quanti2)
        
        
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