
## DEFINIÇÃO ##
# Listas em Python são estruturas de dados que armazenam uma sequência ordenada de elementos mutáveis, ou seja, que podem ser modificadas após a criação.

## PRINCIPAIS CARACTERÍSTICAS ##
# -> Os elementos são organizados de forma linear.
# -> Podem ser acessados pelo índice.
# -> O índice inicia à partir de 0.
# -> Pode conter tipos primitivos (int, float, string e lógicos) e complexos (listas, dicionários, tuplas e objetos).
# -> Os elementos são separados por vírgula.
# -> Inicia e finaliza com colchetes [].

# BIBLIOTECAS UTILIZADAS PELOS MÉTODOS
import random


## MÉTODOS E OPERAÇÕES 

# 03/11/2025
# ITEM 1 - Criação de uma lista vazia
# ITEM 2 - Criação de uma lista com conteúdo pré-definido
# ITEM 3 - Adiciona um Elementos ao Final da Lista
# ITEM 4 - Adiciona um elemento em qualquer lugar da lista
# ITEM 5 - Embaralhando os elementos de uma lista
# ITEM 6 - Obtendo um elemento aleatório de uma lista

# 04/11/2025
# ITEM 7 - Ordenando os elementos de uma lista
# ITEM 8 - Removendo elementos de uma lista utilizando o método remove()
# ITEM 9 - Removendo elementos de uma lista utilizando o método pop()
# ITEM 10 - Removendo elementos de uma lista utilizando o método del()
# ITEM 11 - Fazendo cópia de uma lista (Clonar)
# ITEM 12 - Comparando listas

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 1 - Criação de uma lista vazia
# Sintaxe básica:   <lista> = []
# Exemplo:
# nome_lista = []                                                         # cria uma variável recebendo colchetes vazios. 
# print(f"Exemplo de Lista vazia: {nome_lista}")                          # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 2 - Criação de uma lista com conteúdo pré-definido
# Sintaxe básica:   <lista> = [<elemento1>,<elemento2>,<elemento3>,<elementoN>]
# Exemplo:
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]                # cria uma variável recebendo os valores pré-definidos. 
# print(f"Exemplo de lista com valores pré-definidos: {nome_lista}")      # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 3 - Adiciona um Elementos ao Final da Lista
# Método:           append()
# Sintaxe básica:   <lista>.append(<elemento>)
# Exemplo:  
# nome_lista = []                                                         # cria uma variável recebendo colchetes vazios.
# nome_lista.append("Valor_Metodo_Append")                                # adiciona um novo elemento no final da lista
# print(f"Exemplo de lista com Append: {nome_lista}")                     # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 4 - Adiciona um elemento em qualquer lugar da lista
# Método:           insert()
# Sintaxe básica:   <lista>.insert(<índice>,<elemento>)
# Exemplo: 
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]                # cria uma variável recebendo os valores pré-definidos.
# nome_lista.insert(2, "Valor_Metodo_Insert")                             # adiciona um novo elemento no índice informado da lista
# print(f"Exemplo de lista com Insert: {nome_lista}")                     # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 5 - Embaralhando os elementos de uma lista
# Método:           random.shuffle()
# Sintaxe básica:   <lista>.shuffle(<lista>)
# Obs.:         antes de ser executado, necessita que seja importado a biblioteca random.
# Exemplo:
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]              # cria uma variável recebendo os valores pré-definidos.
# random.shuffle(nome_lista)                                            # chama o método shuffle da biblioteca random passando a lista como parâmetro. 
# print(f"Exemplo de lista embaralhada: {nome_lista}")                  # imprime o conteúdo da lista.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 6 - Obtendo um elemento aleatório de uma lista
# Método:           random.choice()
# Sintaxe básica:   <lista>.choice(<lista>)
# Obs.:         antes de ser executado, necessita que seja importado a biblioteca random.
# Exemplo:
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]              # cria uma variável recebendo os valores pré-definidos.
# elemento_sorteado = random.choice(nome_lista)                         # cria uma variável que recebe o retorno do método choice da biblioteca random passando a lista como parâmetro
# print(f"Exemplo de elemento sorteado: {elemento_sorteado}")           # imprimir o elemento sorteado da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 7 - Ordenando os elementos de uma lista
# Método:           sort()
# Sintaxe básica:   <lista>.sort(reverse = [False | True])
# Observação:       Caso não informe o parâmetro reverse, a ordenação será crescente.
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]         # cria uma variável recebendo os valores pré-definidos.
# nome_lista.sort(reverse = False)                                      # ordena a lista em ordem crescente
# print(f"Exemplo de lista ordenada crescente: {nome_lista}")           # imprime os valores da lista
# nome_lista.sort(reverse = True)                                       # ordena a lista em ordem decrescente
# print(f"Exemplo de lista ordenada decrescente: {nome_lista}")         # imprime os valores da lista
# nome_lista.sort()                                                       # teste de ordenação sem a passagem de parâmetro
# print(nome_lista)                                                       # imprime os valores da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 8 - Removendo elementos de uma lista utilizando o método remove()
# Método:           remove()
# Sintaxe básica:   <lista>.remove(<elemnto>)
# Observação:       Deveremos informar o conteúdo do elemento
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]         # cria uma variável recebendo os valores pré-definidos.
# nome_lista.remove("Valor4")                                            # remove o elemento "Valor4"
# print(nome_lista)                                                       # imprime os valores da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 9 - Removendo elementos de uma lista utilizando o método pop()
# Método:           pop()
# Sintaxe básica:   <lista>.pop(<elemento>)
# Observação:       Deveremos informar o índice do elemento       
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]         # cria uma variável recebendo os valores pré-definidos.
# nome_lista.pop(2)                                                       # remove o elemento da posição 2
# print(nome_lista)                                                       # imprime os valores da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 10 - Removendo elementos de uma lista utilizando o método del()
# Função:           del()
# Sintaxe básica:   del(<lista>[índice])
# Observação:       Deveremos informar qual é a lista e o elemento que desejamos excluir. Caso não seja passado o elemento, o método destruirá a variável do tipo lista.       
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]         # cria uma variável recebendo os valores pré-definidos.
# del(nome_lista[4])                                                      # remove o elemento da posição 4
# print(nome_lista)                                                       # imprime os valores da lista
# del(nome_lista)                                                         # exclui a variável 
# print(nome_lista)                                                       # imprime os valores da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 11 - Fazendo cópia de uma lista (Clonar)
# Função:           list()
# Sintaxe básica:   list(<lista>)
# Observação:       
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]         # cria uma variável recebendo os valores pré-definidos.
# lista_clonada = list(nome_lista)                                        # clona a lista e atribui a variável lista_clonada
# print(lista_clonada)                                                    # imprime os valores da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 12 - Comparando listas
# Função:           list()
# Sintaxe básica:   list(<lista>)
# Observação:       As listas serão iguais somente se tiverem a mesma quantidade de elementos e todos eles forem iguais.    
# Exemplo:
# lista1 = [1,2,3,4,5]
# lista2 = [1,2,3,4,5]
# lista3 = [1,5,3,4,2]
# lista4 = [1,2,3,4]

# #Verificar se a lista1 e lista2 são iguais
# if lista1 == lista2:
#     print("As listas 1 e 2 são iguais.")
# else:
#     print("As listas 1 e 2 são diferentes.")

# #Verificar se a lista2 e lista3 são iguais
# if lista2 = lista3:
#     print("As listas 2 e 3 são iguais.")
# else:
#     print("As listas 2 e 3 são diferentes.")

# #Verificar se a lista3 e lista4 são iguais
# if lista2 == lista3:
#     print("As listas 3 e 4 são iguais.")
# else:
#     print("As listas 3 e 4 são diferentes.")

