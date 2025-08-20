### dicionarios

#modelo simples
pessoa = {
    'nome': 'murylo',
    'idade': 19,
    'peso': 48
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

#teste de dicionário

import os

mensagens = []

name = input ('Nome: ')

while True:
  #limpando o terminal
  os.system('cls')

  if len(mensagens) > 0:
    for m in mensagens:
      print(m['nome'], '-', m['texto'])

  print ('____________________________')

#obtendo texto
texto = input ('mensagem: ')
if texto == 'fim':
  break

#adicionando mensagem na lista
mensagens.append({
  'nome': nome,
  'texto': texto
})

### Funções

#modelo simples

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input('valor 1:'))
    valor2 = int(input('valor 2:'))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, '+', valor2, '=', resposta)
    

  
