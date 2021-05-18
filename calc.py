print('Calculo de comissão + salario semanal')

salario = []
vendas = []
vendedor = []

while True:
    nome = str(input('Digite o nome do vendedor: '))
    if nome == 'adm':
        break
    vendedor.append(nome)
    vender = 's'
    semana = 200
    while vender == 's':
        num = float(input('Digite o valor da venda: '))
        vendas.append(num)
        semana = semana + (num * 0.09)
        vender = str(input('Deseja adicionar outra venda ?\n'))
        if vender != 's':
            salario.append(semana)
tamanho = len(vendedor)

print('Salarios a pagar de 200 até 1000')
print(', '.join([str(semana) for semana in salario if semana > 200 and semana < 1000 ]))

print('Salarios a pagar de 1000 até 3000')
print(', '.join([str(semana) for semana in salario if semana > 1000 and semana < 3000 ]))

print('Salarios a pagar acima de 3000')
print(', '.join([str(semana) for semana in salario if semana > 3000]))

print(f'Vendedores da Semana {vendedor}\nVendas da Semana {vendas}')

for i in range(tamanho):
    print(f'O vendedor {vendedor}, deverá receber {salario} essa semana.')
