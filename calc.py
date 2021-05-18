print('Calculo de comissão + salario mensal')

salario = []
vendas = []
vendedor = []

while True:
    nome = str(input('Digite o nome do vendedor: '))
    if nome == 'adm':
        break
    vendedor.append(nome)
    vender = 's'
    semana = 1000
    while vender == 's':
        num = float(input('Digite o valor da venda: '))
        vendas.append(num)
        semana = semana + (num * 0.09)
        vender = str(input('Deseja adicionar outra venda ?\n'))
        if vender != 's':
            salario.append(semana)

print('Salarios a pagar de 1000 até 3000')
print(', '.join([str(semana) for semana in salario if semana > 1000 and semana < 3000 ]))

print('Salarios a pagar de 3000 até 7000')
print(', '.join([str(semana) for semana in salario if semana > 3000 and semana < 7000 ]))

print('Salarios a pagar acima de 7000')
print(', '.join([str(semana) for semana in salario if semana > 7000]))

print(f'Vendedores do mês {vendedor}\nVendas do mês {vendas}')

j = 0
for i in vendedor:
    print(f'O vendedor {i}, deverá receber {salario[j]} esse mês.')
    j+=1
