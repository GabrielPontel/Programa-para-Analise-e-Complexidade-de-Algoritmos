import time
from collections import deque


# Implementação de Lista Encadeada
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    #Faz a busca forca bruta na estrutura de lista
    def search(self, elemento):
        lista = self.head
        i = 0
        while lista:
            if lista.data == elemento:
                return i
            lista = lista.next
            i += 1
        return i

    def remove(self, elemento):
        cont = 0
        if not self.head:
            return False, cont
        # O elemento está no inicio? 
        if self.head.data == elemento:
            self.head = self.head.next
            self.size -= 1
            return True, cont
        # Busca o elemento mantendo o rastro do anterior
        lista = self.head
        while lista.next:
            cont += 1
            if lista.next.data == elemento:
                lista.next = lista.next.next
                self.size -= 1
                return True, cont 
            lista = lista.next
        return False, cont

# Implementação de Pilha
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def search_purist(self, elemento):
        pilha_aux = Stack()
        pos = -1
        current_distance = 0
        cont= 0

        # Desempilha procurando
        while not self.is_empty():
            cont+=1
            item = self.pop()

            if item == elemento and pos == -1:
                pos = current_distance

            pilha_aux.push(item)
            current_distance += 1

        # Restaura a pilha
        while not pilha_aux.is_empty():
            cont +=1
            self.push(pilha_aux.pop())

        return pos, cont


# Implementação de Fila
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def buscar_na_fila(self, elemento):
        for i, item in enumerate(self.items):
            if item == elemento:
                return i
        return i


# Funções de teste de performance
def test_list_array(n, elemento):
    cont = 0

    # Inserção
    lista = []
    start = time.time()
    for i in range(n):
        lista.append(i)
        cont+=1
    end = time.time()
    insercao = end - start

    #Pesquisa
    start = time.time()
    pos = -1
    for i, valor in enumerate(lista):
        cont+=1
        if valor == elemento:
            pos = i
            break
    end = time.time()
    pesquisa = end - start

    #Remoção
    start = time.time()
    while lista:
        cont += 1
        lista.pop()
    end = time.time()
    remocao = end - start
    return insercao, pesquisa, remocao, cont

def test_linked_list(n, elemento):

    linked_list = LinkedList()
    cont = 0

    # Inserção
    start = time.time()
    for i in range(n):
        cont+=1
        linked_list.append(i)
    end = time.time()
    insercao = end - start

    # Pesquisa
    start = time.time()
    cont += linked_list.search(elemento)
    end = time.time()
    pesquisa = end - start

    # Remoção (todos)
    start = time.time()
    while linked_list.head is not None:
        cont+=1
        bolean, quant= linked_list.remove(linked_list.head.data)
        cont+=quant
    remocao = time.time() - start

    return insercao, pesquisa, remocao, cont

def test_stack(n, elemento):

    stack = Stack()
    cont = 0

    # Inserção (push)
    start = time.time()
    for i in range(n):
        cont += 1
        stack.push(i)
    insercao = time.time() - start
   
    # Pesquisa
    start = time.time()
    pos, quant = stack.search_purist(elemento)
    cont+= quant
    pesquisa = time.time() - start

    # Remoção (pop)
    start = time.time()
    while not stack.is_empty():
        cont+=1
        stack.pop()
    remocao = time.time() - start

    return insercao, pesquisa, remocao, cont


def test_queue(n, elemento):
  
    queue = Queue()
    cont = 0

    # Inserção (enqueue)
    start = time.time()
    for i in range(n):
        cont+=1
        queue.enqueue(i)
    insercao = time.time() - start

     # Pesquisa
    start = time.time()
    cont += queue.buscar_na_fila(elemento)
    pesquisa = time.time() - start

    # Remoção (dequeue)
    start = time.time()
    while not queue.is_empty():
        cont+=1
        queue.dequeue()
    remocao = time.time() - start

    return insercao, pesquisa, remocao, cont

#---------------------------------------------------------------
def medir_dados_estruturas(quantidade, elemento):

    dados = {}

    insercao, pesquisa, remocao, iteracao = test_list_array(quantidade, elemento)
    dados["Vetor"] = {
        "Tempo Inserção": insercao,
        "Tempo Pesquisa": pesquisa,
        "Tempo Remocao": remocao,
        "Tempo (s)": insercao+pesquisa+remocao,
        "Iteracoes":iteracao
    }

    insercao, pesquisa, remocao, iteracao = test_linked_list(quantidade, elemento)
    dados["Lista"] = {
        "Tempo Inserção": insercao,
        "Tempo Pesquisa": pesquisa,
        "Tempo Remocao": remocao,
        "Tempo (s)": insercao+pesquisa+remocao,
        "Iteracoes":iteracao
    }
    
    insercao, pesquisa, remocao, iteracao = test_stack(quantidade, elemento)
    dados["Pilha"] = {
        "Tempo Inserção": insercao,
        "Tempo Pesquisa": pesquisa,
        "Tempo Remocao": remocao,
        "Tempo (s)": insercao+pesquisa+remocao,
        "Iteracoes":iteracao
    }

    insercao, pesquisa, remocao, iteracao = test_queue(quantidade, elemento)
    dados["Fila"] = {
        "Tempo Inserção": insercao,
        "Tempo Pesquisa": pesquisa,
        "Tempo Remocao": remocao,
        "Tempo (s)": insercao+pesquisa+remocao,
        "Iteracoes":iteracao
    }

    return dados