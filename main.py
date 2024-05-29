
print('')

pessoa = {
    'Nome': 'Luís Fernando',
    'Idade': 19,
    'Profissão': 'Autônomo',
    'Gênero': 'Masculino',
    'Cidade': 'Planaltina'
}

del pessoa[input('Informe o nome da chave ao ser deletada:')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

print('')
