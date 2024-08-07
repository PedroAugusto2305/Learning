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

# Dicionários

# A estrutura do dicionário associa valores a chaves, permitindo a rápida recuperação do valor correspondente a uma determinada chave:
empty_dict = {} # Pythonic
empty_dict2 = dict() # menos Pythonic
grades = {"John": 30, "Tyrion": 40} # dicionário literal

# Pesquisando o valor de uma chave:
johns_grade = grades["John"] # é igual 30

# Se procurar uma chave que não está no dicionário ocorrerá um KeyError:
try:
    arya_grade = grades["Arya"]
except KeyError:
    print("no grade for Arya!")

# Podemos verificar a existência de uma chave usando o in:
john_has_grade = "John" in grades # True
arya_has_grade = "Arya" in grades # False

# O método get retorna um valor padrão (em vez de gerar uma exceção) quando procuramos uma chave que não está no dicionário:
johns_grade = grades.get("John", 0) # igual a 30
arya_grade = grades.get("Arya", 0) # igual a 0
no_one_grade = grades.get("No one") # o padrão é None

# Também é possível atribuir pares de valor-chave usando os colchetes:
grades["Tyrion"] = 43 # substiui o valor anterior
grades["Arya"] = 22  # adiciona uma terceira entrada
num_students = len(grades) # igual a 3

# Os dicionários podem representar dados estruturados:
tweet = {
    "user": "JohnSnow",
    "text": "Dracarys",
    "retweet_count": 100,
    "hashtags": ["#got", "#houseStark", "#north", "targaryen"]
}

# Podemos procurar por chaves específicas:

tweet_keys = tweet.keys() # iterável para as chaves
tweet_values = tweet.values() # iterável para os valores
tweet_items = tweet.items() # iterável para as tuplas (chave, valor)

"user" in tweet_keys # True, mas não é Pythonic
"user" in tweet # forma Pythonic de verificar as chaves
"johnSnow" in tweet_values # True (lento, mas é a única forma de verificar)

# defaultdict

from collections import defaultdict

word_counts = defaultdict(int) # int() produz 0
document = ()
for word in document:
    word_counts[word] += 1

# Também é possível usar esse recurso em list, dict e outras funções:
dd_list = defaultdict(list) # list() produz uma lista vazia
dd_list[2].append(1) # agora o dd_list contém {2: [1]}

dd_dict = defaultdict(dict) # dict() produz um dicionário vazio
dd_dict["John"]["House"] = "Stark" # {"John": {"House": "Stark"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1 # agora dd_pair contém {2: [0, 1]}

# Contadores

from collections import Counter

c = Counter([0, 1, 2, 0]) # c é (basicamente) {0: 2, 1: 2, 2: 1}

word_counts = Counter(document)

# Uma instância Counter contém um método most_common bastante útil:

for word, count in word_counts.most_common(10): # imprime as 10 palavras mais comuns e suas contagens
    print(word, count)

# Conjuntos

primes_below_10 = {2, 3, 5, 7}

s = set() # representa um conjunto vazio
s.add(1) # s agora é {1}
s.add(2) # s agora é {1, 2}
s.add(2) # s ainda é {1, 2}
x = len(s) # igual a 2
y = 2 in s # True
z = 3 in s # False

hundreds_of_other_words = {"whatever other words"}
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list # False, mas verifica todos os elementos

stopwords_set = set(stopwords_list)
"zip" in stopwords_set # verificação muito rápida

# Encontrando itens distintos em uma coleção:
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]

# Fluxo de controle

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'" 
else:
    message = "when all else fails use else (if you want to)" 

# ternario:
parity = "even" if x % 2 == 0 else "odd"

# while:
x = 0

while x < 10:
    print(f"{x} is less than 10")
    x += 1

# for e in:
for x in range(10):
    print(f"{x} is less than 10")

# também podemos
for x in range(10):
    if x == 3: 
        continue # vá imediatamente para a próxima iteração
    if x == 5:
        break # saia do loop totalmente
    print(x) # imprimirá 0, 1, 2 e 4

# Veracidade

one_is_less_than_two = 1 < 2 # igual a True
true_equals_false = True == False # igual a False

# None indica um valor que não existe
x = None
assert x == None, "esta não é uma forma Pythonic de verificar o None"
assert x is None, "esta é a forma Pythonic de verificar o None"

def some_function_that_returns_a_string():
    return "Random string..."

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

# esta é uma forma mais breve (e talvez mais complexa) de fazer a mesma coisa:
first_char = s and s[0]

safe_x = x or 0

safe_x = x if x is not None else 0

# função all que retorna true quando todos os elementos são verdadeiros, função any retorna true quando há pelo menos um elemento verdadeiro:
all([True, 1, {3}]) # True, todos são verdadeiros
all([True, 1, {}]) # False, {} é falso
any([True, 1, {}]) # True, true é verdadeiro
all([]) # True, não há nenhum elemento falso na lista
any([]) # False, não há nenhum elemento verdadeiro na lista

# Classificação

x = [4, 1, 2, 3]

y = sorted(x) # y é [1, 2, 3, 4] e x não mudou
x.sort() # x agora é [1, 2, 3, 4]

# classifique a lista por valor absoluto do maior para o menor
x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # é [-4, 3, -2, 1]

# classifique as palavras e contagens do maior número para o menor:
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)

# Compreensões de Listas

# As compreensões de lista são a forma Pythonic de transformar uma lista em outra:
even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]
squares = [x * x for x in range(5)] # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers] # [0, 4, 16]

# Da mesma forma podemos transformar listas em conjuntos ou dicionários:
square_dict = {x: x * x for x in range(5)} # {0: 1, 1: 1, 2: 4, 3: 9, 4: 16}
square_set = {x * x for x in [1, -1]} # {1}

# Quando não precisamos do valor da lista, usamos um _ como variável:
zeros = [0 for _ in even_numbers]  # tem o mesmo tamanho de even_numbers

# uma compreensão de lista pode conter múltiplos fors:
pairs = [(x, y) for x in range(10) for y in range(10)] # 100 pares (0,0), (0,1), ..., (9,8), (9,9)

# os fors posteriores podem usar os resultados dos anteriores:
increasing_pairs = [(x, y) for x in range(10) for y in range(x + 1, 10)]

# Testes Automatizados e asserção

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"

# declaração de que uma função está funcionando:
def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

# outro uso menos comum:
def smallest_item1(xs):
    assert xs, "empty list has smallest item"
    return min(xs)

# Programação Orientada a Objetos

class CountingClicker:
    """ A classe pode/deve ter um docstring, como as funções"""
    def __init__(self, count = 0):
        self.count = count
    
    def _repr_(self):
        return f"CountingClicker(count={self.count})"
    
    def click(self, num_times = 1):
        """Clique no contador algumas vezes"""
        self.count += num_times

    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0
    

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

class NoResetClicker(CountingClicker):
    """Essa classe possuí os mesmos metodos da CountingClicker porém seu método reset não faz nada"""
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

# Iteráveis e Geradores

def generate_range(n):
    i = 0
    while i < n:
        yield i # cada chamada para yield produz um valor do gerador
        i += 1
    
for i in generate_range(10):
    print(f"i: {i}")

# com um gerador é possível criar uma sequência infinita:
def natural_numbers():
    """retorna 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

# Também é possível criar geradores colocando compreensões de for entre parênteses:
evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# Nenhuma das computações abaixo fazem "nada" até a iteração:
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# e assim por diante...

# função enumerate que transforma os valores em pares (index, value):
names = ["Alice", "Bob", "Charlie", "Debbie"]

# não é Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# também não é Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")

# Pythonic
for i, name in enumerate(names):
     print(f"name {i} is {names[i]}")

# Aleatoriedade

import random

random.seed(10) # assim, obteremos sempre os mesmos resultados

four_uniform_randoms = [random.random() for _ in range(4)] # produz números uniformemente entre 0 e 1.

# o módulo random gera números pseudoaleatórios (ou seja, deterministicos) com base em um estado interno que pode ser definido com o random.seed() para obter resultados reproduzíveis:
random.seed(10) # define a semente em 10
print(random.random()) # 0.57140259469
random.seed(10) # redefine a semente em 10
print(random.random()) # 0.57140259469 novamente

# também usaremos o random.randrange, que recebe um ou dois argumentos e retorna um elemento escolhido aleatoriamente no range correspondente:
random.randrange(10) # seleciona aleatoriamente no range(10) = [0, 1, 2, 3, ..., 9]
random.randrange(3, 6) # seleciona aleatoriamente no range(3, 6) = [3, 4, 5]

# meétodo que reordena elementos de uma lista
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten) # estará reordenada de forma aleatoria

# metodo para escolher um elemento em uma lista
my_best_friend = random.choice(["Alice", "Bob", "Charlie", "Debbie"])

# para escolher uma amostra de elementos sem substituição (especialmente sem repetição) usamos o random.sample:
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)

# para escolher uma amostra com substituição:
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)

# Expressões Regulares

# todos são true, porque 'cat' não começa com 'a', 'cat' contém um 'a' e 'dog' não contém um 'c'
re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carvs")), # divide em a ou b para ['c', 'r', 's']
    "R-D-" == re.sub("[0, 9]", "-", "R2D2") # substitui os digitos por traços
]

assert all(re_examples), "all the regex examples should be True"

# Zip e Descompactação de Argumento

# a função zip transforma vários iteráveis em apenas um iterável de tuplas da função correspondente:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# como o zip é lento, temos que fazer algo parecido com:
[pair for pair in zip(list1, list2)] # resultado: [('a', 1), ('b',2), ('c',3)]

# também podemos "extrair" uma lista usando um truque incomum:
pairs = [('a', 1), ('b',2), ('c',3)]
letters, numbers = zip(*pairs) # o asterisco executa a descompactação de argumento

# seria o mesmo que chamar:
letters, numbers = zip(('a', 1), ('b',2), ('c',3))

# é possível usar a descompactação de argumento com qualquer função:
def add(a, b): return a + b

add(1, 2) # retorna 3

try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")

add(*[1, 2]) # retorna 3

# Args e Kwargs

def doubler(f):
    """Aqui, definimos uma nova função que mantém uma referência a f"""
    def g(x):
        return 2 * f(x)
    
    # retornando a nova função
    return g

# Isso pode funcionar em alguns casos

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equals 8"
assert g(-1) == 0, "(-1 + 1) * 2 shoul qual 0"

# não funciona em funções que recebem mais de um argumento:
def f2(x, y): return x + y

g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")

# precisamos especificar uma função que receba argumentos arbitrários. Podemos fazer isso usando a descompactação de argumento e um pouco de mágica:
def magic(*args, **kwargs): 
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

# isso também funciona ao contrário, quando queremos usar uma list (ou tuple) e um dict para fornecer argumentos a uma função:
def other_way_magic(x, y, z): return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

# isso é aplicado para funções de alta ordem que recebem argumentos arbitrários:
def doubler_correct(f):
    """funciona para qualquer entrada recebida por f"""
    def g(*args, **kwargs):
        """todo argumento fornecido para g deve ser transmitido para f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"

# Anotações de Tipo

# Python é uma linguagem dinamicamente tipada, então não importa quais os tipos dos objetos, se eles forem utilizados corretamente:
def add(a, b):
    return a + b

assert add(10, 5) == 15, "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3], "+ is valid for lists"
assert add("hi", "there") == "hi there", "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("cannot add an int to a string")

# em linguagens tipadas estáticamente, as funções e objetos têm tipos específicos:
def add(a: int, b: int) -> int:
    return a + b

add(10, 5) # issod eve estar OK
add("hi", "there") # isso não deve estar OK

# import typing

# def total(xs: List[float]) -> float:
#     return sum(total)

# x: int = 5
