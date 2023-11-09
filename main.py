# nome = input('Digite seu nome: ')
# idade = int(input('Digite seu idade: '))
# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite seu altura: '))
# lista = [nome, idade, peso, altura]
# print(lista)
#
# print('Questão 1')
# print(lista[1])
#
# print('Questão 2')
# sobrenome = input('Digite seu sobrenome: ')
# lista = [nome + ' ' + sobrenome, idade, peso, altura]
# print(lista)
#
# print('Questão 3')
# imc = lista[2] / lista[3]**2
# print(f'IMC é = {imc}')

# carrinho = ['Mouse', 'Teclado', 'Monitor']
# print(f'Seu carrinho tem {len(carrinho)} itens')
# print(carrinho)
# carrinho.append('Fone')
# print(carrinho)
# carrinho.remove('Fone')
# print(carrinho)

# carrinho = []
# while True:
#     item = input('Informe o nome do item: ')
#     carrinho.append(item)
#     print('Produto adicionado com sucesso!')
#     opcao = input('Tecle 1 para sair: ')
#     if opcao == '1':
#         break
# print(carrinho)

# numeros = []
# for i in range(10):
#     item = float(input(f'Digite um numero {i+1}: '))
#     if item % 2 == 0:
#         numeros.append(item)
# print(numeros)

# velocidades = []
# for i in range(10):
#     item = int(input(f'Digite a {i+1}ª velocidade: '))
#     if item > 60:
#         velocidades.append(item)
# print(velocidades)

# lista = ['Fone', 'Mouse', 'Teclado', 'Monitor']
# lista.pop()
# lista.pop(0)
# print(lista)

# lista = ['Fone', 'Mouse', 'Teclado', 'Monitor']
# print(lista)
# item = input('Digite o nome do item que deseja remover: ').capitalize()
# if item in lista:
#     lista.remove(item)
#     print(lista)
# else:
#     print('Item não encontrado!')

# lista = ['Fone', 'Mouse', 'Teclado', 'Monitor']
# for produto in lista:
#     print(produto)

print('Questão 1')
lista = [10, 20, 35, 37, 39, 21, 22, 26, 24, 28, 29]
for i in lista:
    if i % 2 == 0:
        print(i)
print('----------------')
print('Questão 2')
velocidades = [46, 32, 48, 62, 63, 33, 45, 36, 45, 68]
for i in velocidades:
    if i > 60:
        print(i)
print('----------------')
print('Questão 3')
count = 0
for i in lista:
    if i % 2 == 0:
        count += 1
print(f'Quantidade de numeros pares é {count}')
print('----------------')
print('Questão 4')
maior = 0
for i in velocidades:
    if i > maior:
        maior = i
print(f'O maior numero é {maior}')
print('----------------')

print('Desafio')
numeros = [2, 3, 5, 7, 11, 12, 18, 13, 20, 22]
count2 = 0
for i in numeros:
    if i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        count2 += 1
print(f'A quantidade de numeros primos é {count2}')
print('----------------')

print('Desafio 2')
count3 = 0
count4 = 0
for i in numeros:
    for u in range(1, i+1):
            count3 += 1
            if count3 == 2:
                count4 += 1


print(count4)

# carrinho = []
# while True:
#     print('-- Bem vindo ao menu --')
#     print('1 - Adicionar produto')
#     print('2 - Editar produto')
#     print('3 - Remover produto')
#     print('4 - Listar todos os produtos')
#     print('5 - Sair')
#     opcao = input('Selecione a opção: ')
#     if opcao == '1':
#         produto = input('Digite o nome do produto: ')
#         carrinho.append(produto)
#         print('Produto adicionado com sucesso!')
#     elif opcao == '2':
#         produto = input('Digite o produto que deseja editar: ')
#         if produto in carrinho:
#             indice = carrinho.index(produto)
#             carrinho[indice] = input('Digite o nome do produto: ')
#             print('Produto editado com sucesso!')
#         else:
#             print('Produto não encontrado!')
#     elif opcao == '3':
#         produto = input('Digite o produto que deseja remover: ')
#         if produto in carrinho:
#             carrinho.remove(produto)
#             print('Produto removido com sucesso! ')
#         else:
#             print('Produto não encontrado!')
#     elif opcao == '4':
#         print('---- Seu carrinho ----')
#         for produto in carrinho:
#             print(f'Nome do produto: {produto}')
#     elif opcao == '5':
#         print('Você saiu do programa')
#         break


