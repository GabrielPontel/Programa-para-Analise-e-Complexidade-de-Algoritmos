import time
import random

def bubble_sort(arr):
    """
    Implementação do Bubble Sort
    Complexidade: O(n²)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    cont = 0

    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            cont += 1
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                trocou = True
        if not trocou:
            break

    return cont


def bubble_sort_optimized(arr):
    """
    Implementação do Bubble Sort Otimizado (Cocktail Sort)
    Ordena em ambas as direções em cada passagem
    Complexidade: O(n²) no pior caso, mas melhor performance na prática
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    inicio = 0
    fim = n - 1
    trocou = True
    cont = 0

    while trocou and inicio < fim:
        trocou = False

        # Passagem da esquerda para direita
        for i in range(inicio, fim):
            cont += 1
            if arr_copy[i] > arr_copy[i + 1]:
                arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                trocou = True

        if not trocou:
            break

        fim -= 1
        trocou = False

        # Passagem da direita para esquerda
        for i in range(fim, inicio, -1):
            cont += 1
            if arr_copy[i] < arr_copy[i - 1]:
                arr_copy[i], arr_copy[i - 1] = arr_copy[i - 1], arr_copy[i]
                trocou = True

        inicio += 1

    return cont


def selection_sort(arr):
    """
    Implementação do Selection Sort
    Complexidade: O(n²)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    cont = 0 

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            cont += 1
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]

    return cont


def insertion_sort(arr):
    """
    Implementação do Insertion Sort
    Complexidade: O(n²)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    cont = 0

    for i in range(1, n):
        chave = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > chave:
            cont += 1
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = chave

    return cont


def merge_sort(arr):
    """
    Implementação do Merge Sort
    Complexidade: O(n log n)
    """
    arr_copy = arr.copy()

    if len(arr_copy) <= 1:
        return arr_copy, 0

    meio = len(arr_copy) // 2
    esquerda, it_esq = merge_sort(arr_copy[:meio])
    direita, it_dir = merge_sort(arr_copy[meio:])
    resultado, cont = merge(esquerda,direita)
    return resultado, cont+it_esq+it_dir


def merge(esquerda, direita):
    """
    Função auxiliar para merge sort que combina duas listas ordenadas
    """
    resultado = []
    i = j = 0
    cont=0
    while i < len(esquerda) and j < len(direita):
        cont+=1
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado, cont


def quick_sort(arr):
    """
    Implementação do Quick Sort
    Complexidade: O(n log n) no caso médio, O(n²) no pior caso
    """
    arr_copy = arr.copy()

    if len(arr) <= 1:
        return arr, 0

    pivo = arr[len(arr) // 2]

    menores = []
    iguais = []
    maiores = []

    iteracoes = 0

    for x in arr:
        iteracoes += 1  
        if x < pivo:
            menores.append(x)
        elif x == pivo:
            iguais.append(x)
        else:
            maiores.append(x)

    esq, it_esq = quick_sort(menores)
    dir, it_dir = quick_sort(maiores)

    return esq + iguais + dir, iteracoes + it_esq + it_dir

def gerar_array_aleatorio(tamanho, minimo=0, maximo=1000):
    """Gera um array com números aleatórios"""
    return [random.randint(minimo, maximo) for _ in range(tamanho)]


def medir_dados_ordenacao(tamanho):
    """
    Compara o desempenho dos três algoritmos de ordenação
    """
    # Gera array aleatório
    arr = gerar_array_aleatorio(tamanho)
    dados = {}

    # Teste Bubble Sort
    inicio = time.time()
    qtd_iteracoes = bubble_sort(arr)
    fim = time.time() 
    dados["Bubble"]={
        "Tempo (s)": fim - inicio,
        "Iteracoes": qtd_iteracoes,
        "Complexidade": "O(n²)"
    }

    # Teste Bubble Sort Otimizado
    inicio = time.time()
    qtd_iteracoes = bubble_sort_optimized(arr)
    fim = time.time() 
    dados["Bubble+"]={
        "Tempo (s)": fim - inicio,
        "Iteracoes": qtd_iteracoes,
        "Complexidade": "O(n²)"
    }

    # Teste Selection Sort
    inicio = time.time()
    qtd_iteracoes = selection_sort(arr)
    fim = time.time() 
    dados["Selection"]={
        "Tempo (s)": fim - inicio,
        "Iteracoes": qtd_iteracoes,
        "Complexidade": "O(n²)"
    }

    # Teste Insertion Sort
    inicio = time.time()
    qtd_iteracoes = insertion_sort(arr)
    fim = time.time() 
    dados["Insertion"]={
        "Tempo (s)": fim - inicio,
        "Iteracoes": qtd_iteracoes,
        "Complexidade": "O(n²)"
    }

    # Teste merge Sort
    inicio = time.time()
    ordenado, qtd_iteracoes = merge_sort(arr)
    fim = time.time() 
    dados["Merge"]={
        "Tempo (s)": fim - inicio,
        "Iteracoes": qtd_iteracoes,
        "Complexidade": "O(n log(n))"
    }

    # Teste quick Sort
    inicio = time.time()
    ordenado,qtd_iteracoes = quick_sort(arr)
    fim = time.time() 
    dados["Quick"]={
        "Tempo (s)": fim - inicio,
        "Iteracoes": qtd_iteracoes,
        "Complexidade": "O(n log(n))"
    }

    return dados