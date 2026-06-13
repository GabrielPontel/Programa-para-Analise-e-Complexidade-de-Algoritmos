from Gerenciamento_dados.manipulacao_de_graficos import plotar_grafico_iteracao, plotar_grafico_tempo, criar_tabela
from Algoritmos.primos import medir_dados_primos
from Algoritmos.busca import medir_dados_buscas
from Algoritmos.fibonacci import medir_dados_fibonacci
from Algoritmos.fatorial import medir_dados_fatoriais
from Algoritmos.ordenacao import medir_dados_ordenacao
from Algoritmos.estruturas import medir_dados_estruturas
from Interface.complementares import abrir_janela_entrada_geral, abrir_janela_entrada_busca
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def limpar_frame(frame_pai):
    #limpa os frames antigos
    for widget in frame_pai.winfo_children():
        widget.destroy()


def exibir_na_tela(frame_pai, figura_matplotlib):
    limpar_frame(frame_pai)
    frame = FigureCanvasTkAgg(figura_matplotlib, master=frame_pai)
    frame.draw()
    frame.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def gerar_resultado(dados, titulo, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    #lista de algoritmos
    algoritmos = list(dados.keys())
    #dados[Algoritmo][Qualificativo]:valor
    tempos = [dados[alg]["Tempo (s)"] for alg in algoritmos]
    iteracoes = [dados[alg]["Iteracoes"] for alg in algoritmos]

    fig1 = plotar_grafico_tempo(algoritmos, tempos)
    fig2 = plotar_grafico_iteracao(algoritmos, iteracoes)
    criar_tabela(frame_tabela, dados, titulo)

    exibir_na_tela(frame_grafico_tempo, fig1)
    exibir_na_tela(frame_grafico_iteracoes, fig2)


def acao_botao_busca(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    qtd_elementos, elemento_desejado = abrir_janela_entrada_busca(root)
    #Se o usuario fechou a janela
    if qtd_elementos is None or elemento_desejado is None:
        return

    dados = medir_dados_buscas(qtd_elementos, elemento_desejado)
    gerar_resultado(dados, "Comparação de Algoritmos para Busca",
                    frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes)


def acao_botao_primos(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    qtd_elementos = abrir_janela_entrada_geral(root, "Digite a Quantidade de Elementos do Vetor:")

    if qtd_elementos is None:
        return

    dados = medir_dados_primos(qtd_elementos)
    gerar_resultado(dados, "Comparação de Algoritmos para encontrar os Números Primos", frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes)


def acao_botao_fatorial(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    qtd_elementos = abrir_janela_entrada_geral(root, "Digite um Número para encontrar seu Fatorial:")

    if qtd_elementos is None:
        return
    dados = medir_dados_fatoriais(qtd_elementos)
    gerar_resultado(dados, "Comparação de Algoritmos para Fatorial",frame_tabela,frame_grafico_tempo, frame_grafico_iteracoes)


def acao_botao_fibonacci(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    qtd_elementos = abrir_janela_entrada_geral(root, "Digite um número para encontrar seu valor de Fibonacci:")
    if qtd_elementos is None:
        return
    dados = medir_dados_fibonacci(qtd_elementos)
    gerar_resultado(dados, "Comparação de Algoritmos para Fibonacci", frame_tabela, frame_grafico_tempo,frame_grafico_iteracoes)


def acao_botao_estruturas(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    qtd_elementos, elemento = abrir_janela_entrada_busca(root)
    if qtd_elementos is None or elemento is None:
        return
    dados = medir_dados_estruturas(qtd_elementos, elemento)
    gerar_resultado(dados, "Comparação de Estruturas de Dados", frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes)


def acao_botao_ordenacao(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    qtd_elementos = abrir_janela_entrada_geral(root, "Digite a Quantidade de Elementos:")
    if qtd_elementos is None:
        return
    dados = medir_dados_ordenacao(qtd_elementos)
    gerar_resultado(dados, "Comparação de Algoritmos de Ordenação", frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes)