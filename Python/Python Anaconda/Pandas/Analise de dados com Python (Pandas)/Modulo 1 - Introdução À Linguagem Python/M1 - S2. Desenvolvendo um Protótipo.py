# #! Desenvolvendo um Protótipo
# #? Ao tabular os dados do gráfico, aparece um valor interessante na coluna que mostra o aumento mês após mês. De acordo com as informações o aumento tem sido constante.

# #? Se o aumento é constante, podemos usar uma função do primeiro grau para prever qual será o resultado em qualquer mês. A função será r = c * mes, onde, r é o resultado que queremos, c é a constante de crescimento e mes é a variável de entrada. Dessa forma, ao obter um mês qualquer (2, 4, 30, etc) podemos dizer qual o resultado.

# #? Vamos testar nossa fórmula:

# #? mes = 2; c = 200 -> r = 200 * 2 = 400 (Valor correto para o mês 2.
# #? mes = 3; c = 200 -> r = 200 * 3 = 600 (Valor correto para o mês 3.
# #? mes = 4; c = 200 -> r = 200 * 4 = 800 (Valor correto para o mês 4.
# #? mes = 5; c = 200 -> r = 200 * 5 = 1000 (Valor correto para o mês 5.


# #* Mês     Resultado   Aumento
# #* 1       200         -
# #* 2       400         200
# #* 3       600         200
# #* 4       800         200
# #* 5       1000        200
# #* 6       1200        200


c = 200 # valor da constante

mes = input("Digite o mês que deseja saber o resultado: ") # Função para captura o mês que o cliente digitar
mes = int(mes) # Não esqueça de converter para numérico o valor captura pela função input()

r = c * mes # Equação do primeiro grau, também chamada função do primeiro grau ou de função linear.

print(f"A quantidade de peças para o mês {mes} será {r}") # Impressão do resultado usando string interpolada "f-strings" (PEP 498)

# Desafio da internet
# Que tal treinar um pouco mais de programação e conhecer novas fontes de informações? Você, aluno, tem acesso à Biblioteca Virtual, um repositório de livros e artigos que pode ser acessado no endereço: (http://biblioteca-virtual.com/).

# Na página 47 (capítulo 2: Objetos e Comandos de Entrada e Saída em Python) da obra: BANIN, S. L. Python 3 - conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018, você encontra o exercício proposto 1. Utilize o emulador a seguir, para resolver o desafio!

# Utilize o emulador a seguir, para resolver o desafio!