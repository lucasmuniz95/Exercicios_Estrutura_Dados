ano = int(input('Digite um ano bissexto: '))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('\nEsse ano é bissexto')
else:
    print('\nEsse ano não é bissexto')
