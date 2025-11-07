
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

# 06/11/2025
# ITEM 13 - Clonando e comparando listas
# ITEM 14 - Incluindo elementos de uma lista em outra
# ITEM 15 - Ocorrências de elementos e comprimento da lista
# ITEM 16 - Menor elemento de uma lista 
# ITEM 17 - Maior elemento de uma lista 
# ITEM 18 - Soma dos elementos de uma lista 

# 07/11/2025
# ITEM 19 - Retornando o índice de um elemento
# ITEM 20 - Retornando índice e elemento
# ITEM 21 - Listas aninhadas


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 1 - Criação de uma lista vazia
# Sintaxe básica:   <lista> = []
# Exemplo:
# nome_lista = []                                                       # cria uma variável recebendo colchetes vazios. 
# print(f"Exemplo de Lista vazia: {nome_lista}")                        # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 2 - Criação de uma lista com conteúdo pré-definido
# Sintaxe básica:   <lista> = [<elemento1>,<elemento2>,<elemento3>,<elementoN>]
# Exemplo:
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]              # cria uma variável recebendo os valores pré-definidos. 
# print(f"Exemplo de lista com valores pré-definidos: {nome_lista}")    # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 3 - Adiciona um Elementos ao Final da Lista
# Método:           append()
# Sintaxe básica:   <lista>.append(<elemento>)
# Exemplo:  
# nome_lista = []                                                       # cria uma variável recebendo colchetes vazios.
# nome_lista.append("Valor_Metodo_Append")                              # adiciona um novo elemento no final da lista
# print(f"Exemplo de lista com Append: {nome_lista}")                   # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 4 - Adiciona um elemento em qualquer lugar da lista
# Método:           insert()
# Sintaxe básica:   <lista>.insert(<índice>,<elemento>)
# Exemplo: 
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]               # cria uma variável recebendo os valores pré-definidos.
# nome_lista.insert(2, "Valor_Metodo_Insert")                            # adiciona um novo elemento no índice informado da lista
# print(f"Exemplo de lista com Insert: {nome_lista}")                    # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 5 - Embaralhando os elementos de uma lista
# Método:           random.shuffle()
# Sintaxe básica:   <lista>.shuffle(<lista>)
# Obs.:         antes de ser executado, necessita que seja importado a biblioteca random.
# Exemplo:
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]               # cria uma variável recebendo os valores pré-definidos.
# random.shuffle(nome_lista)                                             # chama o método shuffle da biblioteca random passando a lista como parâmetro. 
# print(f"Exemplo de lista embaralhada: {nome_lista}")                   # imprime o conteúdo da lista.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 6 - Obtendo um elemento aleatório de uma lista
# Método:           random.choice()
# Sintaxe básica:   <lista>.choice(<lista>)
# Obs.:         antes de ser executado, necessita que seja importado a biblioteca random.
# Exemplo:
# nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]               # cria uma variável recebendo os valores pré-definidos.
# elemento_sorteado = random.choice(nome_lista)                          # cria uma variável que recebe o retorno do método choice da biblioteca random passando a lista como parâmetro
# print(f"Exemplo de elemento sorteado: {elemento_sorteado}")            # imprimir o elemento sorteado da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 7 - Ordenando os elementos de uma lista
# Método:           sort()
# Sintaxe básica:   <lista>.sort(reverse = [False | True])
# Observação:       Caso não informe o parâmetro reverse, a ordenação será crescente.
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]        # cria uma variável recebendo os valores pré-definidos.
# nome_lista.sort(reverse = False)                                       # ordena a lista em ordem crescente
# print(f"Exemplo de lista ordenada crescente: {nome_lista}")            # imprime os valores da lista
# nome_lista.sort(reverse = True)                                        # ordena a lista em ordem decrescente
# print(f"Exemplo de lista ordenada decrescente: {nome_lista}")          # imprime os valores da lista
# nome_lista.sort()                                                      # teste de ordenação sem a passagem de parâmetro
# print(nome_lista)                                                      # imprime os valores da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 8 - Removendo elementos de uma lista utilizando o método remove()
# Método:           remove()
# Sintaxe básica:   <lista>.remove(<elemnto>)
# Observação:       Deveremos informar o conteúdo do elemento
# Exemplo:
# nome_lista = ["Valor5", "Valor3", "Valor4", "Valor1", "Valor2"]         # cria uma variável recebendo os valores pré-definidos.
# nome_lista.remove("Valor4")                                             # remove o elemento "Valor4"
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

## Verificar se a lista1 e lista2 são iguais
# if lista1 == lista2:
#     print("As listas 1 e 2 são iguais.")
# else:
#     print("As listas 1 e 2 são diferentes.")

## Verificar se a lista2 e lista3 são iguais
# if lista2 == lista3:
#     print("As listas 2 e 3 são iguais.")
# else:
#     print("As listas 2 e 3 são diferentes.")

## Verificar se a lista3 e lista4 são iguais
# if lista2 == lista3:
#     print("As listas 3 e 4 são iguais.")
# else:
#     print("As listas 3 e 4 são diferentes.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Incluir o conteúdo dos estudos abaixo:

# 06/11/2025
# ITEM 13 - Clonando e comparando listas
# ITEM 14 - Incluindo elementos de uma lista em outra
# ITEM 15 - Ocorrências de elementos e comprimento da lista
# ITEM 16 - Menor elemento de uma lista 
# ITEM 17 - Maior elemento de uma lista 
# ITEM 18 - Soma dos elementos de uma lista 


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 19 - Retornando o índice de um elemento
# Função:           index()
# Sintaxe básica:   <lista>.index(<elemento>)
# Observação:       Retorna a primeira ocorrência do elemento informado.
# Exemplo:
# lista = [1,2,3,4,5]
# procurar_por = 3
# indice = lista.index(procurar_por)
# print(indice)

# Demostração manual da mesma operação sem usar a função
# lista = [1,2,3,4,5,2]
# procurar_por = 2
# for indice, valor in enumerate(lista):
#     print(f"Teste do índice {indice}")
#     if valor == procurar_por:
#         print(indice)
#         break

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 20 - Retornando índice e elemento
# Função:           index()
# Sintaxe básica:   <lista>.index(<elemento>)
# Observação:       
# Exemplo:
# lista = ["A","B","C","D"]
# for chave, valor in enumerate(lista): 
#     print(f"Posição: {chave} Valor: {valor}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 21 - Listas aninhadas
# Função:           index()
# Sintaxe básica:   <lista>.index(<elemento>)
# Observação:       
# Exemplo:
# lista = ["A","B",["C","D"],["E","F"]]
# print(lista[0]) # -> VALOR: "A"

lista = ["A","B","C","D",["E","F"]]
procurar_por = "E"
# Cria um range de 0 até o tamanho da lista, e faz um loop atribuindo a variável indiceLista o valor do range atual.
for indiceLista in range(0, len(lista)): 
    # Imprime o conteúdo do elemento da lista na posição indicada pela variável indiceLista.
    print(f"Índice lista: {indiceLista} - Valor: {lista[indiceLista]}") 
    # Verifica na lista se o conteúdo do elemento na posição indicada pela variável indiceLista é igual ao conteúdo da variável procurar_por
    if lista[indiceLista] == procurar_por:
        # Se for igual irá imprimir no terminal a mensagem "Achou". 
        print("Achou") 
    # Se a verificação do if for falsa, ele vai verificar se o elemento na posição indicada pela variável indiceLista é uma instância da classe LIST.
    elif isinstance(lista[indiceLista], list): 
        # Cria um range de 0 até o tamanho do elemento na posição indicada pela variável indiceLista, e faz um loop atribuindo a variável indiceSubLista o valor do range atual. 
        for indiceSubLista in range(0, len(lista[indiceLista])):
            # Imprimi a mensagem abaixo informando o índice da lista externa, o índice da lista interna e o conteúdo da lista interna 
            print(f"Índice lista: {indiceLista} - Índice sub-lista: {indiceSubLista} Valor: {lista[indiceLista][indiceSubLista]}")
            # Verificar se o conteúdo da lista interna é igual ao conteúdo da variável procurar_por.
            # Para acessar o conteúdo da sub-lista é necessário informar o índice da lista externa e o índice da lista interna onde o conteúdo está localizado. Exemplo: lista[indiceListaExterna][indiceListaInterna]
            if lista[indiceLista][indiceSubLista] == procurar_por:
                # Imprimir a mensagem "Achou"
                print("Achou")


