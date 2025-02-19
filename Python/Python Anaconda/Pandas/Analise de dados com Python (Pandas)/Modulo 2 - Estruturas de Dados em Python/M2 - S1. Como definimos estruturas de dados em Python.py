# #! M.2 -  em Python?
def divisoria(txt):
    print("\n","="*(len(txt)+4),"\n  ",txt,"\n","="*(len(txt)+4),"\n")

# ==============================================
divisoria("In[1]:")
# ==============================================
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"texto = {texto}")  # Saída: texto = Aprendendo Python na disciplina de linguagem de programação.
print(f"Tamanho do texto = {len(texto)}")  # Saída: Tamanho do texto = 60
print(f"Python in texto = {'Python' in texto}")  # Saída: Python in texto = True
print(f"Quantidade de y no texto = {texto.count('y')}")  # Saída: Quantidade de y no texto = 1
print(f"As 5 primeiras letras são: {texto[0:6]}")  # Saída: As 5 primeiras letras são: Aprend
print(f"As letras de 10 a 15 são: {texto[9:15]}")  # Saída: As letras de 10 a 15 são: Python
print(f"A última letra é: {texto[-1]}")  # Saída: A última letra é: .
print(f"A penúltima letra é: {texto[-2]}")  # Saída: A penúltima letra é: o

# ==============================================
divisoria("In[2]:")
# ==============================================
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"texto = {texto}")  # Saída: texto = Aprendendo Python na disciplina de linguagem de programação.
print(texto.upper())  # Saída: APRENDENDO PYTHON NA DISCIPLINA DE LINGUAGEM DE PROGRAMAÇÃO.
print(texto.replace("i", 'XX'))  # Saída: Aprendendo Python na dXXscXXplXXna de lXXnguagem de programação.
print(texto.replace("Python", "Java"))  # Saída: Aprendendo Java na disciplina de linguagem de programação.
print(texto.replace("a", "X", 2))  # Saída: Xprendendo Python nX disciplina de linguagem de programação.
print(texto.split())  # Saída: ['Aprendendo', 'Python', 'na', 'disciplina', 'de', 'linguagem', 'de', 'programação.']
print(texto.split('a'))  # Saída: ['Aprendendo Python n', ' disciplin', ' de lingu', 'gem de progr', 'mação.']
print(texto.split(' '))  # Saída: ['Aprendendo', 'Python', 'na', 'disciplina', 'de', 'linguagem', 'de', 'programação.']
print(texto.split(' ', 2))  # Saída: ['Aprendendo', 'Python', 'na disciplina de linguagem de programação.']

# ==============================================
divisoria("In[3]:")
# ==============================================
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"texto = {texto}")  # Saída: texto = Aprendendo Python na disciplina de linguagem de programação.
print(f"Tamanho do texto = {len(texto)}\n")  # Saída: Tamanho do texto = 60

palavras = texto.split()
print(f"palavras = {palavras}")  # Saída: palavras = ['Aprendendo', 'Python', 'na', 'disciplina', 'de', 'linguagem', 'de', 'programação.']
print(f"Tamanho de palavras = {len(palavras)}")  # Saída: Tamanho de palavras = 8

# ==============================================
divisoria("In[4]:")
# ==============================================
texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""
print(f"Tamanho do texto = {len(texto)}")  # Saída: Tamanho do texto = 297
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
lista_palavras = texto.split()
print(f"Tamanho da lista de palavras = {len(lista_palavras)}")  # Saída: Tamanho da lista de palavras = 47

total = lista_palavras.count("string") + lista_palavras.count("strings")
print(f"Quantidade de vezes que string ou strings aparecem = {total}")  # Saída: Quantidade de vezes que string ou strings aparecem = 3

# ==============================================
divisoria("In[5]:")
# ==============================================
vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')  
        # Saída: Posição = 0, valor = a
        # Saída: Posição = 1, valor = e
        # Saída: Posição = 2, valor = i
        # Saída: Posição = 3, valor = o
        # Saída: Posição = 4, valor = u


# ==============================================
divisoria("In[6]:")
# ==============================================
# Mesmo resultado.
vogais = []
print(f"Tipo do objeto vogais = {type(vogais)}")  # Saída: Tipo do objeto vogais = <class 'list'>

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}") 
        # Saída: Posição = 0, valor = a
        # Saída: Posição = 1, valor = e
        # Saída: Posição = 2, valor = i
        # Saída: Posição = 3, valor = o
        # Saída: Posição = 4, valor = u

# ==============================================
divisoria("In[7]:")
# ==============================================
frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

print("maça" in frutas)  # Saída: True
print("abacate" in frutas)  # Saída: False
print("abacate" not in frutas)  # Saída: True
print(min(frutas))  # Saída: banana
print(max(notas))  # Saída: 10
print(frutas.count("maça"))  # Saída: 2
print(frutas + notas)  # Saída: ['maça', 'banana', 'uva', 'mamão', 'maça', 8.7, 5.2, 10, 3.5]
print(2 * frutas)  # Saída: ['maça', 'banana', 'uva', 'mamão', 'maça', 'maça', 'banana', 'uva', 'mamão', 'maça']

# ==============================================
divisoria("In[8]:")
# ==============================================
lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

print(f"Tamanho da lista = {len(lista)}")  # Saída: Tamanho da lista = 6

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -> tipo individual = {type(item)}") 
        # Saída: Posição = 0,	    valor = Python             -> tipo individual = <class 'str'>
        # Saída: Posição = 1,	    valor = 30.61              -> tipo individual = <class 'float'>
        # Saída: Posição = 2,	    valor = Java               -> tipo individual = <class 'str'>
        # Saída: Posição = 3,	    valor = 51                 -> tipo individual = <class 'int'>
        # Saída: Posição = 4,	    valor = ['a', 'b', 20]     -> tipo individual = <class 'list'>
        # Saída: Posição = 5,	    valor = maça               -> tipo individual = <class 'str'>

print("\nExemplos de slices:\n")    # Saída: Exemplos de slices:

print("lista[1]    = ", lista[1])       # Saída: lista[1]    = 30.61
print("lista[0:2]  = ", lista[0:2])     # Saída: lista[0:2]  = ['Python', 30.61]
print("lista[:2]   = ", lista[:2])      # Saída: lista[:2]   = ['Python', 30.61]
print("lista[3:5]  = ", lista[3:5])     # Saída: lista[3:5]  = [51, ['a', 'b', 20]]
print("lista[3:6]  = ", lista[3:6])     # Saída: lista[3:6]  = [51, ['a', 'b', 20], 'maça']
print("lista[3:]   = ", lista[3:])      # Saída: lista[3:]   = [51, ['a', 'b', 20], 'maça']
print("lista[-2]   = ", lista[-2])      # Saída: lista[-2]   = ['a', 'b', 20]
print("lista[-1]   = ", lista[-1])      # Saída: lista[-1]   = maça
print("lista[4][1] = ", lista[4][1])    # Saída: lista[4][1] = b

# ==============================================
divisoria("In[9]:")
# ==============================================
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() # Essa sintaxe produz o mesmo resultado que a linha 1
print("Antes da listcomp = ", linguagens)  # Saída: Antes da listcomp = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

linguagens = [item.lower() for item in linguagens]
print("\nDepois da listcomp = ", linguagens)  # Saída: Depois da listcomp = ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']

# ==============================================
divisoria("In[10]:")
# ==============================================
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print("Antes da listcomp = ", linguagens)  # Saída: Antes da listcomp = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()
    
print("\nDepois da listcomp = ", linguagens)  # Saída: Depois da listcomp = ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']

# ==============================================
divisoria("In[11]:")
# ==============================================
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = [item for item in linguagens if "Java" in item]

print(linguagens_java)  # Saída: ['Java', 'JavaScript']

# ==============================================
divisoria("In[12]:")
# ==============================================
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java = []

for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)

print(linguagens_java)  # Saída: ['Java', 'JavaScript']

# ==============================================
divisoria("In[13]:")
# ==============================================
# Exemplo 1
print("Exemplo 1")  # Saída: Exemplo 1
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")  # Saída: A nova lista é = <map object at 0x...>

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")  # Saída: Agora sim, a nova lista é = ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']


# Exemplo 2
print("\n\nExemplo 2")  # Saída: Exemplo 2
numeros = [0, 1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x*x, numeros))
print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")  # Saída: Lista com o número elevado a ele mesmo = [0, 1, 4, 9, 16, 25]


# ==============================================
divisoria("In[14]:")
# ==============================================
numeros  = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# ==============================================
divisoria("In[15]:")
# ==============================================
#! TUPLAS
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")  # Saída: Tipo do objeto vogais = <class 'tuple'>

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")  # Saída: Posição = 0, valor = a
                                         # Saída: Posição = 1, valor = e
                                         # Saída: Posição = 2, valor = i
                                         # Saída: Posição = 3, valor = o
                                         # Saída: Posição = 4, valor = u

# ==============================================
divisoria("In[16]:")
# ==============================================
# Se usarmos da forma abaixo, teremos um erro, pois tuplas são imutáveis
    #?vogais = ()
    #?vogais.append('a')
    #!----> 3 vogais.append('a')
    #!AttributeError: 'tuple' object has no attribute 'append'

# ==============================================
divisoria("In[17]:")
# ==============================================
# Devemos declaras as tuplas com todos os elementos que desejamos, pois não podemos adicionar elementos posteriormente
vogais = ('a', 'e', 'i', 'o', 'u')
for item in enumerate(vogais):
    print(item) # Saída: (0, 'a')
                # Saída: (1, 'e')
                # Saída: (2, 'i')
                # Saída: (3, 'o')
                # Saída: (4, 'u')
    
print(tuple(enumerate(vogais)))
print(list(enumerate(vogais)))


#? Objetos do tipo Set
#? A tradução"conjunto" para set  nos leva diretamente à essência desse tipo de estrutura de dados em Python. Um objeto do tipo set habilita operações matemáticas de conjuntos, tais como: união, intersecção, diferenteça, etc. Esse tipo de estrutura pode ser usado, portanto, em testes de associação e remoção de valores duplicados de uma sequência (PSF, 2020c).
#? Das operações que já conhecemos sobre sequências, conseguimos usar nessa nova estrutura:
#? len(s)
#? x in s
#? x not in s
##? Além dessas operações, podemos adicionar um novo elemento a um conjunto com a função add(valor). Também podemos remover com remove(valor). Veja uma lista completa de funções no endereço https://bit.ly/2NF7eIT.
#? Em Python, os objetos do tipo set podem ser construídos destas maneiras:
#? Usando um par de chaves e elementos separados por vírgulas: set1 = {'a', 'b', 'c'}
#? Usando o construtor de tipo: set(iterable)
#? Não é possível criar um set vazio, com set = {}, pois essa é a forma de construção de um dicionário. Para construir com utilização da função set(iterable), obrigatoriamente temos de passar um objeto iterável para ser transformado em conjunto. Esse objeto pode ser uma lista, uma tupla ou até mesmo uma string (que é um tipo de sequência). Veja os exemplos de construção a seguir.

# ==============================================
divisoria("In[18]:")
divisoria("Construção de objetos do tipo set")
# ==============================================
vogais_1 = {'aeiou'} # sem uso do construtor
print("vogais_1:", type(vogais_1), vogais_1)  # Saída: <class 'set'> {'aeiou'}

vogais_2 = set('aeiouaaaaaa') # construtor com string
print("vogais_2:" ,type(vogais_2), vogais_2)  # Saída: <class 'set'> {'e', 'a', 'i', 'o', 'u'}

vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print("vogais_3:",type(vogais_3), vogais_3)  # Saída: <class 'set'> {'e', 'a', 'i', 'o', 'u'}

vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print("vogais_4:",type(vogais_4), vogais_4)  # Saída: <class 'set'> {'e', 'a', 'i', 'o', 'u'}

print(set('banana'))  # Saída: {'b', 'a', 'n'}

#? Na entrada 18 (In [18]), criamos 4 exemplos de construção de objetos set. Com exceção do primeiro, no qual não usamos o construtor set(), os demais resultam na mesma estrutura. Veja que, no exemplo 2, passamos como parâmetro uma sequência de caracteres 'aeiouaaaaaa' e, propositalmente, repetimos a vogal a. O construtor interpreta como um iterável e cria um conjunto em que cada caractere é um elemento, eliminando valores duplicados. Veja, na linha 13, o exemplo no qual transformamos a palvra 'banana' em um set, cujo resultado é a eliminação de caracteres duplicados.

#! EXEMPLIFICANDO
#? O poder do objeto set está em suas operações matemáticas de conjuntos. Vejamos um exemplo: uma loja de informática recebeu componentes usados de um computador para avaliar se estão com defeito. As peças que não estiverem com defeito podem ser colocadas à venda. Como, então, podemos criar uma solução em Python para resolver esse problema? A resposta é simples: usando objetos do tipo set. Observe o código a seguir.

# ==============================================
divisoria("In[19]:")
# ==============================================
#? EXEMPLO DE USO DE SETS
def create_report():
    componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])
    
    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)
    
    componentes_ok = componentes_verificados.difference(componentes_com_defeito)
    
    print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")  # Saída: Foram verificados 23 componentes.
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")  # Saída: 4 componentes apresentaram defeito.
    
    print("Os componentes que podem ser vendidos são:")  # Saída: Os componentes que podem ser vendidos são:
    for item in componentes_ok:
        print(item)  # Saída: [lista de componentes ok, um por linha]


create_report()


#? Na entrada 19 (In [19]), criamos uma função que gera o relatório das peças aptas a serem vendidas. 
#? Nessa função, são criados dois objetos set: "componentes_verificados" e "componentes_com_defeito". 
#? Nas linhas 5 e 6, usamos a função len() para saber quantos itens há em cada conjunto. 
#? Na linha 8, fazemos a "mágica"! Usamos a função difference() para obter os itens que estão em componentes_verificados, mas não em componentes_com_defeito.
#? Essa operação também poderia ser feita com o sinal de subtração: componentes_ok = componentes_verificados - componentes_com_defeito. Com uma única operação conseguimos extrair uma importante informação!

#! Objetos do tipo mapping
# As estruturas de dados que possuem um mapeamento entre uma chave e um valor são consideradas objetos do tipo mapping. Em Python, o objeto que possui essa propriedade é o dict (dicionário). Uma vez que esse objeto é mutável,  conseguimos atribuir um novo valor a uma chave já existente.

# Podemos construir dicionários em Python das seguintes maneiras:

# Usando um par de chaves para denotar um dict vazio: dicionario1 = {}
# Usando um par de elementos na forma, chave : valor separados por vírgulas: dicionario2 = {'one': 1, 'two': 2, 'three': 3}
# Usando o construtor de tipo: dict()
# Observe os exemplos a seguir com maneiras de construir o dicionário.

# ==============================================
divisoria("In[20]:")
# ==============================================

# Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor 
dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30

# Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
dici_2 = {'nome': 'João', 'idade': 30}

# Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
dici_3 = dict([('nome', "João"), ('idade', 30)])

# Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.
dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))

print(f"dici_1 = {dici_1.get('nome')}")
print(f"dici_2 = {dici_2.keys()}")
print(f"dici_3 = {dici_3.values()}")
print(f"dici_4 = {dici_4.items()}")
print(f"dici_4 = {dici_4}")

print(dici_1 == dici_2 == dici_3 == dici_4) # Testando se as diferentes construções resultamo em objetos iguais.