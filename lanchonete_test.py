import sys


escolha=[]
cardapio = {"coca": 4, "pastel": 6}
escolha.append(cardapio)

itens=[] ## produtos
quantidade=[] ## quantidade dos itens
multi=[] ##valor do produto vezes a quantidade


print("-"*20,"LANCHONETE","-"*20)
print('')
print("CARDAPIO:")
print('')
for cardapio in escolha:
    for a, b in cardapio.items():
        print(a + ": "+str(b))
        print(16*"-")

while True:
    
    try:
        pedido = input("qual o pedido?")
        itens.append(pedido)
        
        while True:
            quan = int(input("quantidade ?"))
            if quan >0:
                quantidade.append(quan)
                break
    
            else:
                ("")        
        print('-'*30)

        pagar=cardapio[pedido] * quan
        multi.append(pagar)
        final=sum(multi)

       
        s_n=str(input('Deseja comprar algo mais?: [s|n]')).upper
        print(' ')
        if s_n == 'n' or 'nao':
                break
            
    except:
        print("Opa meu amigo, essa não é a resposta correta, tente novamente:")
print(' ')
print("*"*26,"Conta","*"*26)
print('-'*50)
print("Produto:          Quantidade:          Total de cada item:")
for x in range(len(itens)):
    print(itens[x],"            ",quantidade[x],"                  ", multi[x])

print('')
print('-'*59)
print(" "*18,"Valor total da conta: ")
print(" "*26,"R$",sum(multi))
print('-'*59)

 

 