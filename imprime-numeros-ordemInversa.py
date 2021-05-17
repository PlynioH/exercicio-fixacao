print('Este leitor de Números lê uma sequência de números inteiros e os imprime em ordem inversa.')

lista = []
for i in range(10):
    num = int(input('Digite um número: '))
    lista.append(num)
i = 9
while i != -1:
    print(lista[i])
    i-=1
