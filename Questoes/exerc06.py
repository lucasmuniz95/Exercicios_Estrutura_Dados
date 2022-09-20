idade = []
altura = []

for i in range(5):
    idade.append(float(input('Informe sua idade: ')))
    altura.append(float(input('Informe sua altura: ')))

print(f'Idade na ordem inversa: {idade[::-1]}')
print(f'Altura na ordem inversa: {altura[::-1]}')
print(f'Lista de idade: {idade}')
print(f'Lista de altura: {altura}')
