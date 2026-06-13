import time

#-----------------------------------------------------------------

def eh_primo_forca_bruta(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#-----------------------------------------------------------------

def listar_primos_forca_bruta(limite):
    primos = []
    cont = 0
    for num in range(2, limite + 1):
        eh_primo = True
        for i in range(2, num):
            cont += 1
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return cont, len(primos)

#-----------------------------------------------------------------

def crivo_de_eratostenes(limite):
    cont = 0
    if limite < 2:
        return cont, 0

    # Criar lista booleana "primo[0..limite]" e inicializar todos como verdadeiros
    primo = [True] * (limite + 1)
    primo[0] = primo[1] = False

    p = 2
    while p * p <= limite:
        # Se primo[p] não foi alterado, então é primo
        if primo[p]:
            # Marcar todos os múltiplos de p como não primos
            for i in range(p * p, limite + 1, p):
                primo[i] = False
                cont += 1
        p += 1

    primos = [num for num in range(2, limite + 1) if primo[num]]
    return cont, len(primos)

#-----------------------------------------------------------------

def crivo_de_atkin(limite):
    cont = 0

    if limite < 2:
        return cont, []

    # Inicializar o array de primos
    primo = [False] * (limite + 1)

    # Marcar 2 e 3 como primos
    if limite >= 2:
        primo[2] = True
    if limite >= 3:
        primo[3] = True

    # Marcar números usando as equações do Crivo de Atkin
    x = 1
    while x * x <= limite:
        y = 1
        while y * y <= limite:
            cont += 1
            n = 4 * x * x + y * y
            if n <= limite and (n % 12 == 1 or n % 12 == 5):
                primo[n] = not primo[n]

            n = 3 * x * x + y * y
            if n <= limite and n % 12 == 7:
                primo[n] = not primo[n]

            n = 3 * x * x - y * y
            if x > y and n <= limite and n % 12 == 11:
                primo[n] = not primo[n]

            y += 1
        x += 1

    # Marcar múltiplos de quadrados como não primos
    r = 5
    while r * r <= limite:
        if primo[r]:
            for i in range(r * r, limite + 1, r * r):
                cont += 1
                primo[i] = False
        r += 1

    primos = [num for num in range(2, limite + 1) if primo[num]]
    return cont, len(primos)

# -----------------------------------------------------------------

def crivo_eratostenes_lista(limite):
    primo = [True] * (limite + 1)
    primo[0] = primo[1] = False

    for p in range(2, int(limite**0.5) + 1):
        if primo[p]:
            for i in range(p * p, limite + 1, p):
                primo[i] = False

    return [i for i in range(2, limite + 1) if primo[i]]

def crivo_segmentado(limite):
    cont = 0 
    if limite < 2:
        return cont, []

    import math

    # Calcular o limite da raiz quadrada
    raiz_limite = int(math.sqrt(limite)) + 1

    # Usar crivo simples para encontrar primos até raiz_limite
    primos_base = crivo_eratostenes_lista(raiz_limite)

    # Tamanho do segmento
    delta = raiz_limite

    primos = primos_base.copy()

    # Processar cada segmento
    inicio = raiz_limite + 1
    while inicio <= limite:
        fim = min(inicio + delta - 1, limite)

        # Criar array booleano para o segmento atual
        segmento = [True] * (fim - inicio + 1)

        # Marcar múltiplos de cada primo base no segmento
        for primo in primos_base:
            # Encontrar o primeiro múltiplo de primo no segmento
            primeiro_multiplo = ((inicio + primo - 1) // primo) * primo

            # Marcar todos os múltiplos no segmento
            for j in range(primeiro_multiplo, fim + 1, primo):
                cont += 1
                if j >= inicio:
                    segmento[j - inicio] = False

        # Adicionar primos do segmento à lista
        for i in range(len(segmento)):
            if segmento[i]:
                primos.append(inicio + i)

        inicio += delta

    return cont, len(primos)

# -----------------------------------------------------------------

#Função para medir e alocar em um dicionários os nomes dos métodos e seus tempos de execução.
def medir_dados_primos(quantidade):

    dados = {}

    start = time.time()
    qtd_iteracoes, qtd_primos = listar_primos_forca_bruta(quantidade)
    end = time.time()
    dados["Força Bruta"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Quantidade de Primos": qtd_primos,
        "Complexidade": "O(n²)"
    }

    start = time.time()
    qtd_iteracoes, qtd_primos = crivo_de_eratostenes(quantidade)
    end = time.time()
    dados["Eratóstenes"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Quantidade de Primos": qtd_primos,
        "Complexidade": "O(n log n)"
    }



    start = time.time()
    qtd_iteracoes, qtd_primos = crivo_de_atkin(quantidade)
    end = time.time()
    dados["Atkin"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Quantidade de Primos": qtd_primos,
        "Complexidade": "O(n)"
    }


    start = time.time()
    qtd_iteracoes, qtd_primos = crivo_segmentado(quantidade)
    end = time.time()
    dados["Segmentado"] = {
        "Tempo (s)": end - start,
        "Iteracoes": qtd_iteracoes,
        "Quantidade de Primos": qtd_primos,
        "Complexidade": "O(n)"
    }


    return dados
