nome = str(input('Qual é seu nome? '))
if nome == 'Filipe':
    print('Que nome bonito')
elif nome =='pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cludia Michelle Alicia':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))