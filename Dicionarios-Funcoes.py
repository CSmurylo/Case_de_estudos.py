### dicionarios
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




  
