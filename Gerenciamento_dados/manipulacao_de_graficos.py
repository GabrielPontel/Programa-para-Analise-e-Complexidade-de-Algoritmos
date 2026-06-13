import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import tkinter as tk
from tkinter import ttk

#Montar um grafico de barra para o tempo
def plotar_grafico_tempo(algoritmos, tempos):

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    barras = ax.bar(algoritmos, tempos, color='green')

    # Colocando os valores em cima das colunas
    for barra in barras:
        altura_da_coluna = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2,
                altura_da_coluna,
                f"{altura_da_coluna:.6f}",
                ha='center',
                va='bottom',fontsize=12,          
                fontweight='bold',
                color='lightgreen',)

    plt.style.use('seaborn-v0_8')
    ax.set_ylabel("Tempo (s)", fontweight='bold', fontsize='12')
    ax.set_xlabel("Métodos", fontweight='bold', fontsize='12')
    

    return fig

def plotar_grafico_iteracao(algoritmos, iteracoes):

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    barras = ax.bar(algoritmos, iteracoes, color='green')

    # Colocando os valores em cima das colunas
    for barra in barras:
        altura_da_coluna = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2,
                altura_da_coluna,
                f"{altura_da_coluna:.0f}",
                ha='center',
                color='lightgreen',
                va='bottom',
                fontsize=12,          
                fontweight='bold')
    
    ax.set_ylabel("Quantidade de iterações", fontweight='bold', fontsize='12')
    ax.set_xlabel("Métodos", fontweight='bold', fontsize='12')

    return fig


def criar_tabela(frame_pai, dados, titulo):
    # Limpa o frame antes
    for widget in frame_pai.winfo_children():
        widget.destroy()

    label_titulo = tk.Label(frame_pai,text=titulo,font=("Arial", 14, "bold"), bg="#111111", fg="white")
    label_titulo.pack(pady=5)

    # Pega as colunas automaticamente do primeiro item
    primeira_chave = next(iter(dados))
    colunas_dinamicas = list(dados[primeira_chave].keys())

    # Adiciona "Algoritmo" como primeira coluna
    colunas = ["Algoritmo"] + colunas_dinamicas

    tabela = ttk.Treeview(frame_pai, columns=colunas, show="headings")

    # Criar cabeçalhos
    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, anchor="center")

    # Inserir dados
    for metodo, info in dados.items():
        linha = [metodo]

        for col in colunas_dinamicas:
            valor = info.get(col, "-")

            # Formatação especial para tempo
            if col.lower() == "tempo":
                valor = f"{valor:.6f}"

            linha.append(valor)

        tabela.insert("", tk.END, values=linha)

    tabela.pack(fill=tk.BOTH, expand=True)