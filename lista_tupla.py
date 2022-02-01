lista=['banana', 'café', 'nescal']
print(lista)
lista.append('Abacaxi') # adiciona um item 
print(lista)
lista.insert(0,'Abacaxi') #adiciona um item na lista na posição escolhida
print(lista)
lista.remove('nescal') #remove um item
print(lista)
lista.pop(0) #remove o item da casa
print(lista) 
print(lista[1])  #print do item selecionado na casa



for i in lista: # somente com o print(i) printa a lista sem os "" e ()
    print(i, end=' ') # com o end printa um do lado do outro

print('')
print('')
print('')
print('')
print(50*"-")


tupla=('banana', 'café', 'nescal') #lista que não pode ser alteravel
print(tupla)

print(tupla[2]) # acessa um item da tupla pelo index 

for i in tupla: # mesmo esquema 
    print(i)

print('')
print('')
print('')
print('')
print(50*"-")

