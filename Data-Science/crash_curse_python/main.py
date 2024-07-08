"""
Revisão de Python com o livro "Data Science do zero".
Abaixo estão todos os códigos utilizados no capítulo 2: Um Curso Intensivo de Python
"""

# Módulos

import re # importação de um módulo, também é possível usar um alias: import re as regex

my_regex = re.compile("[0-9]+", re.I)

from collections import defaultdict, Counter # também é possível importar funcionalidades específicas de um módulo

lookup = defaultdict(int)
my_counter = Counter()

# Funções

def double(x):
    """
    Em funções é muito comum se colocar docstrings (como essa) que descrevem a função.
    Esta função multiplica a entrada por 2.
    """
    return x * 2

def apply_to_one(f):
    """
    No python as funções são de primeira classe, então podemos atribuir outras funções como argumento
    """
    return f(1)

my_double = double # refere-se à função x já definida
x = apply_to_one(my_double)  # resultado: 2

y = apply_to_one(lambda x: x + 4) # também é possível criar funções lambda, o resultado dessa função é 5

# Os parâmetros da função também podem receber argumentos padrão:
def my_print(message = "Mensagem padrão"):
    print(message)

my_print("Hello") # imprime "Hello"
my_print() # imprime "Mensagem padrão"

# Também é interessante especificar alguns argumentos padrões quando queremos obter um valor diferente:
def full_name(first = "Qual é o seu primeiro nome", last = "Qual é o seu sobrenome"):
    return first + " " + last

full_name("John", "Snow") # "John Snow"
full_name("John") # "John Qual é o seu sobrenome"
full_name(last="Snow") # "Qual é o seu primeiro nome Snow"

# Strings

# É possível adicionar strings com aspas simples ou aspas duplas, é importante manter o mesmo padrão para todo o projeto
single_quoted_string = 'Data Science'
double_quoted_string = "Data Science"

# Podemos codificar caracteres especiais usando barra invertida:
tab_string = "\t" # representa o caractere tab
len(tab_string) # o tamanho é 1

# Também é possível criar strings brutas  com o:
not_tab_string = r"\t" # representa os caracteres "\" e "t"
len(not_tab_string) # o tamanho é 2

# Para criar strings de várias linhas usamos três aspas duplas:
multi_line_string = """Esta é a primeira linha
e esta é a segunda linha,
e esta é a terceira linha.
"""

# Também podemos usar o f-string:
first_name = "John"
last_name = "Snow"

full_name1 = f"{first_name} {last_name}" # "John Snow"

# Exceções

# Quando algo dá errado o Python gera uma exceção, para tratá-las usamos:
try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

# Listas

# Uma lista é uma coleção ordenada de dados
integer_list = [1, 2, 3]
heterogenous_list = ["String", 0.1, True]  # podemos adicionar diversos tipos de dados a uma lista
list_of_list = [integer_list, heterogenous_list, []] # também podem ser adicionadas listas dentro de listas

list_length = len(integer_list) # verifica o tamanho da lista, no caso é 3
list_sum = sum(integer_list) # realiza a soma dos valores dentro da lista que é: 6

# Também podemos definir um elemento n de uma lista usando a notação de colchetes:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0] # igual a 0, as listas são indexadas a partir de 0
one = x[1] # igual a 1
nine = x[-1] # igual a 9, "Pythonic" para o último elemento
eight = x[-2] # iogual a 8, "Pythonic" para o penúltimo elemento
x[0] = -1 # agora x é [-1, 1, 2, 3, ..., 9]

# Também é possível fatiar as listas:
every_third = x[::3] # [-1, 3, 6, 9]
five_to_three = x[5:2:-1] # [5, 4, 3]

# O operador in é usado para verificar a associaçõa à lista:
1 in [1, 2, 3] # True
0 in [1, 2, 3] # False

# Para concatenar uma lista usamos:
x = [1, 2, 3]
x.extend([4, 5, 6]) # agora x = [1, 2, 3, 4, 5, 6]

# Caso não queira modificar a lista:
x = [1, 2, 3]
y = x + [4, 5, 6] # agora y = [1, 2, 3, 4, 5, 6] e x não mudou

# Normalmente acrescentamos item por item na lista:
x = [1, 2, 3]
x.append(0) # x agora é [1, 2, 3, 0]
y = x[-1] # igual a 0
z = len(x) # igual a 4

# Muitas vezes é conveniente descompactar as listas quando sabemos quantos elementos elas contém:
x, y = [1, 2] # agora x é 1, y é 2

# Se não houver o mesmo número de elementos dos dois lados haverá um ValueError, então podemos fazer da seguinte forma:
_, y = [1, 2] # agora y == 2, não considerou o primeiro elemento

# Tuplas

# As tuplas são parecidas com as listas, porém as tuplas não podem ser modificadas.

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4 # também é possível escrever tuplas sem parênteses
my_list[1] = 3 # my_list agora é [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

# podemos usar as tuplas para criar funções que retornam múltiplos valores:
def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3) # o resultado é (5, 6)
s, p = sum_and_product(5, 10) # s é 15, p é 50

# as tuplas (e as listas) também podem ser usadas em atribuições múltiplas:
x, y = 1, 2 # x é 1 e y é 2
x, y = y, x # forma Pythonic de trocar variáveis: agora x é 2 e y é 1


