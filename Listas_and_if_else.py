#SEPARAR OS TRECHOS PARA EVITER CONFLITOS NA HORA DE RODAR OS CÓDIGOS

###listas

lista_numeros = [1, 2, 3]

# posso alterar os valores nelas
lista_numeros[0] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

# podem possuir todos os tipos de dados
numeros = [1, 2, 3]
strings = ['João', 'Maria', 'Bruxa']
decimais = [10.8, 11.5, 15.2]

## >métodos< para usar com listas vazias, no caso, o 'append'.

#append - adiciona um novo item ao final da lista.
lista_vazia = []
lista_vazia.append('olá')
lista_vazia.append('mundo')
print(lista_vazia)

#len/min/max - já descritos do trecho abaixo né
numeros2 = [10, 28, 4, 5, 9, 13]
print('Total de números: ', len(numeros2))
print('Menor número: ', min(numeros2))
print('Maior número: ', max(numeros2))

--------------------------------------------------------------------------------------

salario = float(input("digite seu salário: "))

# if/elif/else e 'and' para juntar mais de um no elif.

if salario <= 3000:
    print('junior')
elif salario > 3000 and salario <= 6000:
    print('pleno')
elif salario > 6000 and salario <= 15000:
    print('senior')
else:
    print('gerente de projetos')

