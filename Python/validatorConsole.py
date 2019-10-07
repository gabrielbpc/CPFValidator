from CPF import CPF

while True:    
    value = input('Digite o CPF:')

    response = CPF().validate(value)

    print('Este CPF eh', 'valido' if response else 'invalido')