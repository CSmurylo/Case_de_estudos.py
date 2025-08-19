#SEPARAR OS TRECHOS DE CÓDIGO FOR/WHILE

###Laços de repetição com for

Notas = []

for x in range(5):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    Notas.append(resultado)
    print('-------------------------------------------------------------')

print('==================================================================')
print('Quanntidade de notas', len(Notas) )
print('==================================================================')

for n in Notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tirou nota:', nota)

-------------------------------------------------------------------------------------------------------------------

##laços com while
notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    #alternativa: contador += 1
    contador = contador + 1
    
print( 'quantidade de notas', len(notas) )
