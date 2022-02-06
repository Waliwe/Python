#Dicionario
person1={"nome":"Mateus","idade":"33","sexo":"masculino"}   #usado para acessar a atribuição dada a um item
person2={"nome":"Larissa","idade":"22","sexo":"feminino"}
print(f'Nome: {person1["nome"]}')
print(f'Idade: {person1["idade"]}')
print(f'Sexo: {person1["sexo"]},{person2["sexo"]}')

print('')
print(50*'-')
print('')

print(person1.get("sobrenome")) #get == pegar, usado para verificar se tem o item no dicionario 
                                #se não tem o item ele da como ''none''

print('')
print(50*'-')
print('')

print(person1.keys()) ## mostra quais são os itens(chaves) do dicionario
print(person1.values()) ##mostra os valores dos itens

print('')
print(50*'-')
print('')

person1["sobrenome"]= "Henrique" #adiciona uma nova chave(item) no dicionario
print(person1.keys())
print(person1)

person1["idade"]= "35" #altera o valor do item(chave)
print(f'Idade: {person1["idade"]}')

print('')
print(50*'-')
print('')

print(len(person1)) ##ve o tamanho da chave (quantos itens tem)

print('')
print(50*'-')
print('')

person1.update({"contato":"222"}) ##adicionar uma chave(item)
print(person1)

person1.update({"sobrenome":"Carvalho"}) ##atualizar uma chave(item)
print(person1)

print('')
print(50*'-')
print('')

person1.pop("nome") ## remove uma chave(item) do dicionario ('.popitem()' remove a ultima chave adicionada)

print(person1.keys())


