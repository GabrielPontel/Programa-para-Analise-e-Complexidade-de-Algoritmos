import time

#-----------------------------------------------------------------

#Faz o fibonacci a parir de um laço
def fibonacci_iterativo(n):
    cont = 0
    if n <= 1:
        return 0, n
    a, b = 0, 1
    for _ in range(2, n + 1):
        cont += 1
        a, b = b, a + b
    return cont,b

#-----------------------------------------------------------------

#Faz o fibonacci a partir de recursões
def fibonacci_recursivo(n, cont=0):
    cont += 1
    if n <= 1:
        return cont, n
    
    c1, v1 = fibonacci_recursivo(n - 1, cont)
    c2, v2 = fibonacci_recursivo(n - 2, cont)
    
    return c1 + c2, v1 + v2

#-----------------------------------------------------------------

#Tem se um vetor para armazenar os fibonacci dos numeros, não precisando repetir esse processo.
def fibonacci_memoizacao(n, memo=None, cont=0):
    cont += 1
    
    if memo is None:
        memo = {}
        
    if n in memo:
        return cont, memo[n]
    
    if n <= 1:
        return cont, n
    
    c1, v1 = fibonacci_memoizacao(n-1, memo, cont)
    c2, v2 = fibonacci_memoizacao(n-2, memo, cont)
    
    memo[n] = v1 + v2
    return c1 + c2, memo[n]

#-----------------------------------------------------------------

#Biblioteca responsavel por realizar o fibonacci_memo
from functools import lru_cache

#O Python cria o cache automaticamente
def fibonacci_memo_contador(n):
    cont = {"valor": 0}  # usamos dicionário para ser mutável

    @lru_cache(None)
    def fib(x):
        cont["valor"] += 1
        
        if x <= 1:
            return x
        return fib(x - 1) + fib(x - 2)

    resultado = fib(n)
    fib.cache_clear()  # limpa o cache depois de usar

    return cont["valor"], resultado

#-----------------------------------------------------------------

#Função para medir e alocar em um dicionários os nomes dos métodos e seus tempos de execução.
def medir_dados_fibonacci(quantidade):
    
    dados = {}

    start = time.time()
    qtd_iteracoes, resultado = fibonacci_iterativo(quantidade)
    end = time.time()

    dados["Iterativo"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Resultado": resultado,
        "Complexidade": "O(n)"
    }

    start = time.time()
    qtd_iteracoes, resultado = fibonacci_recursivo(quantidade)
    end = time.time()

    dados["Recursivo"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Resultado": resultado,
        "Complexidade": "O(n²)"
    }

    start = time.time()
    qtd_iteracoes, resultado = fibonacci_memoizacao(quantidade)
    end = time.time() 

    dados["Memo-Vetor"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Resultado": resultado,
        "Complexidade": "O(n)"
    }

    start = time.time()
    qtd_iteracoes, resultado= fibonacci_memo_contador(quantidade)
    end = time.time()

    dados["Memo-Cache"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Resultado": resultado,
        "Complexidade": "O(n)"
    }

    return dados

