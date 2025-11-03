
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

# ITEM 1 - Criação de uma lista vazia
# ITEM 2 - Criação de uma lista com conteúdo pré-definido
# ITEM 3 - Adiciona um Elementos ao Final da Lista
# ITEM 4 - Adiciona um elemento em qualquer lugar da lista
# ITEM 5 - Embaralhando os elementos de uma lista
# ITEM 6 - Obtendo um elemento aleatório de uma lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 1 - Criação de uma lista vazia
# Exemplo:
nome_lista = []                                                         # cria uma variável recebendo colchetes vazios. 
print(f"Exemplo de Lista vazia: {nome_lista}")                          # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 2 - Criação de uma lista com conteúdo pré-definido
# Exemplo:
nome_lista = ["Valor1", "Valor2", "Valor3", "Valor...N"]                # cria uma variável recebendo os valores pré-definidos. 
print(f"Exemplo de lista com valores pré-definidos: {nome_lista}")      # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 3 - Adiciona um Elementos ao Final da Lista
# Método: append(objeto)
# Exemplo:
nome_lista.append("Valor_Metodo_Append")                                # adiciona um novo elemento no final da lista
print(f"Exemplo de lista com Append: {nome_lista}")                     # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 4 - Adiciona um elemento em qualquer lugar da lista
# Método: insert(indice, objeto)
# Exemplo: 
nome_lista.insert(2, "Valor_Metodo_Insert")                             # adiciona um novo elemento no índice informado da lista
print(f"Exemplo de lista com Insert: {nome_lista}")                     # imprime o conteúdo da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 5 - Embaralhando os elementos de uma lista
# Método:       random.shuffle(objeto)
# Obs.:         antes de ser executado, necessita que seja importado a biblioteca random.
# Exemplo:
random.shuffle(nome_lista)                                              # chama o método shuffle da biblioteca random passando a lista como parâmetro. 
print(f"Exemplo de lista embaralhada: {nome_lista}")                    # imprime o conteúdo da lista.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

## ITEM 6 - Obtendo um elemento aleatório de uma lista
# Método:       random.choice(objeto)
# Obs.:         antes de ser executado, necessita que seja importado a biblioteca random.
# Exemplo:
elemento_sorteado = random.choice(nome_lista)                           # cria uma variável que recebe o retorno do método choice da biblioteca random passando a lista como parâmetro
print(f"Exemplo de elemento sorteado: {elemento_sorteado}")             # imprimir o elemento sorteado da lista

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
