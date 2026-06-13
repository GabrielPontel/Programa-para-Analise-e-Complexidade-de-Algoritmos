import tkinter as tk

# Função para gerar erro caso digite nada ou negativo
def validar_positivo(texto):
    try:
        num = int(texto)

        if num <= 0:
            return False, "Digite um número maior que 0!"

        return True, num

    except ValueError:
        return False, "Digite um número válido!"

def criar_botao(frame, texto, comando):
    return tk.Button(frame,text=texto,command=comando,bg="#333333",fg="white",activebackground="#555555",activeforeground="white",font=("Arial", 10, "bold"),
        width=8,height=2,bd=3,relief="raised")
    

def abrir_janela_entrada_geral(root, pergunta):
    janela = tk.Toplevel(root)
    janela.title("Entrada de Dados")
    janela.geometry("450x300")
    janela.resizable(False, False)

    janela.transient(root)
    janela.grab_set()

    tk.Label(janela, text= pergunta,bg="#2b2b2b",fg="white",font=("Arial", 12)).pack(pady=5)
    entrada_qtd = tk.Entry(janela)
    entrada_qtd.pack(pady=5)

    mensagem_erro = tk.Label(janela, text="", fg="red",bg="#2b2b2b", font=("Arial", 10))
    mensagem_erro.pack()

    valor = {"qtd": None}

    def executar():
        valido_qtd, resultado_qtd = validar_positivo(entrada_qtd.get())
        if not valido_qtd:
            mensagem_erro.config(text=resultado_qtd)
            return

        valor["qtd"] = resultado_qtd

        janela.destroy()

    btn1 = criar_botao(janela, "Executar", executar)
    btn1.pack(pady=10) 

    janela.configure(bg="#2b2b2b")

    root.wait_window(janela)

    return valor["qtd"]

def abrir_janela_entrada_busca(root):
    janela = tk.Toplevel(root)
    janela.title("Entrada de Dados")
    janela.geometry("450x300")
    janela.resizable(False, False)

    janela.transient(root)
    janela.grab_set()

    tk.Label(janela, text="Quantidade de Elementos:",bg="#2b2b2b",fg="white",font=("Arial", 12)).pack(pady=5)
    entrada_qtd = tk.Entry(janela)
    entrada_qtd.pack(pady=5)

    tk.Label(janela, text="Elemento desejado:",bg="#2b2b2b",fg="white",font=("Arial", 12)).pack(pady=5)
    entrada_busca = tk.Entry(janela)
    entrada_busca.pack(pady=5)

    mensagem_erro = tk.Label(janela, text="", fg="red", bg="#2b2b2b", font=("Arial", 10))
    mensagem_erro.pack()

    valor = {"qtd": None, "busca": None}

    def executar():
        valido_qtd, resultado_qtd = validar_positivo(entrada_qtd.get())
        if not valido_qtd:
            mensagem_erro.config(text=resultado_qtd)
            return

        valido_busca, resultado_busca = validar_positivo(entrada_busca.get())
        if not valido_busca:
            mensagem_erro.config(text=resultado_busca)
            return

        valor["qtd"] = resultado_qtd
        valor["busca"] = resultado_busca

        janela.destroy()

    #tk.Button(janela, text="Executar", command=executar).pack(pady=10)
    btn1 = criar_botao(janela, "Executar", executar)
    btn1.pack(pady=10) # pack em vez de grid

    janela.configure(bg="#2b2b2b")

    root.wait_window(janela)

    return valor["qtd"], valor["busca"]

def reproduzir_imagem(frame, caminho_imagem):
    # limpa o frame antes
    for widget in frame.winfo_children():
        widget.destroy()

    # abre a imagem
    imagem = Image.open(caminho_imagem)

    # redimensiona para caber no frame (ajuste se quiser)
    imagem = imagem.resize((1200, 600))

    imagem_tk = ImageTk.PhotoImage(imagem)

    label = tk.Label(frame, image=imagem_tk, bg="black")
    label.image = imagem_tk  # evitar garbage collection
    label.pack(expand=True)

def mostrar_menu_formatado(frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes):
    # limpar tudo
    for frame in [frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes]:
        for widget in frame.winfo_children():
            widget.destroy()

    texto_topo = tk.Label(
        frame_tabela,
        text=(
            "No nosso software, realizamos a comparação entre diferentes tipos de algoritmos,\n"
            "considerando critérios como o número de iterações e o tempo de execução necessário\n"
            "para realizar suas operações, com o objetivo de analisar e compreender a\n"
            "complexidade de cada algoritmo."
        ),font=("Arial", 14, "bold"),fg="white",bg="#111111",justify="center"
    )
    texto_topo.pack(pady=10)

    titulo = tk.Label(
        frame_tabela,
        text="Algoritmos Trabalhados:",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#111111"
    )
    titulo.pack(pady=10)

    esquerda = tk.Label(
        frame_grafico_tempo,
        text=(
            " -> Busca: Binária e Linear\n\n"
            " -> Primos: Força Bruta, Crivo de Eratóstenes, \n Crivo de Atkin e Crivo Segmentado\n\n"
            " -> Estruturas: Lista, Pilha, Fila e Array"
        ),font=("Arial", 14, "bold"),fg="white",bg="#111111",justify="left")
    esquerda.pack(padx=20, pady=20, anchor="nw")

    direita = tk.Label(
        frame_grafico_iteracoes,
        text=(
            " -> Fatorial: Recursivo e Iterativo\n\n"
            " -> Fibonacci: Recursivo e Iterativo,\n"
            " Cache e memoização\n\n"
            " -> Ordenação: Bubble Sort, Bubble Sort Otimizado, Selection Sort,\n"
            " Insertion Sort, Merge Sort e Quick Sort"
        ),
        font=("Arial", 14, "bold"),fg="white",bg="#111111",justify="left")
    direita.pack(padx=20, pady=20, anchor="nw")