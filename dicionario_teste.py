person1={'nome': 'Mateus', 'idade': '35', 'sexo': 'masculino', 'sobrenome': 'Henrique', 'contato': '3333'}

for x in person1: ## define que o person1 é o x e mostra as chaves
    print(x, end=" ")

print('')
print(50*'-')
print('')

for x in person1.values(): 
    print(x, end=" ") #printa os valores de x(person1)

print('')
print(50*'-')
print('')

for x,y in person1.items(): ## printa o dicionario com as chaves e valores
    print(x,y)

print('')
print(50*'-')
print('')

clientenovo=person1.copy() ## copia os dados de um dicionario para outro 
print(clientenovo)

print('')
print(50*'-')
print('')


alunos={"aluno1": {"nome": "Joao", "idade":"12"}, "aluno2": {"nome":"maria", "idade":"13"}} #adiciona um dicionario dentro de outro
for x,y in alunos.items():
    print(x,y)

print('')
print(50*'-')
print('')

alunos.clear()  ##limpa as chaves do dicionario 
print(alunos)