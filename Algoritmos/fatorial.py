import time

#-----------------------------------------------------------------

#Detem o fatorial a partir de um laço
def fatorial_iterativo(n):
    cont = 0
    resultado = 1
    for i in range(2, n+1):
        cont+=1
        resultado *= i
    return cont, resultado

#-----------------------------------------------------------------

#Detem o fatorial a partir de recurções
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1, 1  # (cont, resultado)

    cont, resultado = fatorial_recursivo(n - 1)
    return cont + 1, n * resultado

#-----------------------------------------------------------------

#Função para medir e alocar em um dicionários os nomes dos métodos e seus tempos de execução.
def medir_dados_fatoriais(quantidade):
    dados = {}

    start = time.time()
    qtd_iteracoes, resultado = fatorial_iterativo(quantidade)
    end = time.time()
    dados["Iterativo"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Resultado": resultado,
        "Complexidade": "O(n)"
    }

    start = time.time()
    qtd_iteracoes, resultado = fatorial_recursivo(quantidade)
    end = time.time()
    dados["Recursivo"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Resultado": resultado,
        "Complexidade": "O(n)"
    }

    return dados

