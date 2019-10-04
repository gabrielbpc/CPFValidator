from validator import Validator

value = input('Digite o CPF:')

response = Validator.validate(value)

print('Este CPF é ' + 'valido' if response else 'invalido')