
escolha=[]
cardapio = {"coca": 4, "pastel": 6}
escolha.append(cardapio)

itens=[] ## produtos
quantidade=[] ## quantidade dos itens
multi=[] ##valor do produto vezes a quantidade


print("-"*20,"LANCHONETE","-"*20)
print('')
print("-"*20,"CARDAPIO",20*"-")
print('')
for cardapio in escolha:
    for a, b in cardapio.items():
        print(a + ": "+str(b))
        print(16*"-")

while True:
    pedido = input("qual o pedido?")
    itens.append(pedido)
    quan = int(input("quantidade ?"))
    quantidade.append(quan)
    print('-'*30)

    pagar = {cardapio[pedido] * quan}
    multi.append(pagar)
    
    valor=sum(pagar)
    
    s_n=str(input('Deseja comprar algo mais?: [s|n]'))
    print(' ')
    if s_n == 'n':
        break

print(' ')
print('Sua lista: ')
print('')

for x in range(len(itens)):
    print("Voce comprou",quantidade[x],'itens do produto: (',itens[x], ') no valor de:')
    
