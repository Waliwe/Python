numeros = list()
for i in range(1,101):
    numeros.append(i)
    
for item in numeros:
    if item%2 == 1:
        continue
    print (item)





    
while True:
    try:
        pedido=str(input("Qual o seu pedido? ('lanche', 'refri')"))
        if pedido == 'lanche':
            print("deu 5:30")
            break
            
        if pedido == "corote":
            idade=int(input('Digite sua idade: '))
            if idade >= 18:
                print("deu 4:30")
                
            else:
                print('não vendemos para menores')
            break
        else:
            print('esse pedido não esta disponivel')
            print('tente novamente')
    except ValueError:
        print('Não é uma idade válida')