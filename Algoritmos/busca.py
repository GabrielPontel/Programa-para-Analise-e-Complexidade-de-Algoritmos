import time

#-----------------------------------------------------------------

#Algoritmo de busca binária, no qual recebe um vetor e um elemento
#E retorna caso ache a posição do elemento, se não retorna -1.
def busca_binaria(arr, alvo):
    esquerda, direita = 0, len(arr) - 1
    cont = 0
    while esquerda <= direita:
        cont+=1
        meio = (esquerda + direita) // 2
        if arr[meio] == alvo:
            return cont, meio
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return cont, -1

#-----------------------------------------------------------------

#Algoritmo de busca linear, no qual recebe um vetor e um elemento
#E retorna caso ache a posição do elemento, se não retorna -1.
def busca_linear(lista, elemento):
    cont = 0
    for i in range(0, len(lista)-1):
        cont += 1
        if lista[i] == elemento:
            return cont, i
    return cont, -1

#-----------------------------------------------------------------

#Função para medir e alocar em um dicionários os nomes dos métodos e seus tempos de execução.
def medir_dados_buscas(quantidade, elemento):

    arr = list(range(quantidade))
    dados = {}

    start = time.time()
    qtd_iteracoes, pos = busca_linear(arr, elemento)
    end = time.time()
    dados["Busca Linear"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Posição do Elemento": 'Não contém o elemento' if pos == -1 else pos,
        "Complexidade": "O(n)"
    }


    start = time.time()
    qtd_iteracoes, pos = busca_binaria(arr, elemento)
    end = time.time()
    dados["Busca Binaria"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Posição do Elemento": 'Não contém o elemento' if pos == -1 else pos,
        "Complexidade": "O(log n)"
    }


    return dados
