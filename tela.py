import tkinter as tk
from Interface.complementares import (criar_botao, mostrar_menu_formatado)
from Gerenciamento_dados.acoes import (limpar_frame,acao_botao_busca,acao_botao_primos,acao_botao_fatorial,acao_botao_fibonacci,acao_botao_estruturas,acao_botao_ordenacao)

#Principal
root = tk.Tk()
root.title("Análise e Complexidade de Algoritmos")
root.geometry("1400x900")
root.configure(bg="#2b2b2b")

frame_container = tk.Frame(root, bg="#2b2b2b")
frame_container.pack(fill=tk.BOTH, expand=True)

frame_tv = tk.Frame(frame_container, height=1000, bg="black", bd=8, relief="ridge")
frame_tv.pack(pady=20, anchor="center")

#O texto que tem em cima na TV
label_tv = tk.Label(frame_tv,text="📺 Análise e Complexidade de Algoritmos",bg="black",fg="white",font=("Arial", 16, "bold"))
label_tv.pack(pady=5)

#Parte da tabel
frame_tabela = tk.Frame(frame_tv,width=1200, height=200,bg="#111111",bd=2,relief="solid")
frame_tabela.pack(pady=10)
frame_tabela.pack_propagate(False)

#Para separar os graficos
frame_borda_interna = tk.Frame(frame_tv,bg="black", bd=5)
frame_borda_interna.pack(pady=10)

#Parte destinada aos graficos
frame_graficos = tk.Frame(frame_borda_interna,bg="#111111", width=1300,height=370)
frame_graficos.pack()
frame_graficos.pack_propagate(False)

# grafico tempo
frame_grafico_tempo = tk.Frame( frame_graficos, width=640, height=370,bg="#111111")
frame_grafico_tempo.pack(side=tk.LEFT)
frame_grafico_tempo.pack_propagate(False)

# grafico iterações
frame_grafico_iteracoes = tk.Frame(frame_graficos, width=640,height=370, bg="#111111")
frame_grafico_iteracoes.pack(side=tk.RIGHT)
frame_grafico_iteracoes.pack_propagate(False)

#Botões
frame_botoes = tk.Frame(frame_container, bg="#2b2b2b")
frame_botoes.pack(pady=15, fill=tk.X)

#Para permitir o espaçamento entre os botaos
for i in range(7):
    frame_botoes.grid_columnconfigure(i, weight=1)

btn0 = criar_botao(frame_botoes,"Menu",lambda: mostrar_menu_formatado(frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn0.grid(row=0,column=0, padx=5, pady=5, sticky="ew")

btn1 = criar_botao(frame_botoes,"Busca",lambda: acao_botao_busca(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn1.grid(row=0,column=1, padx=5, pady=5, sticky="ew")

btn2 = criar_botao(frame_botoes,"Primos", lambda: acao_botao_primos(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn2.grid(row=0,column=2, padx=5,pady=5, sticky="ew")

btn3 = criar_botao(frame_botoes,"Fatorial",    lambda: acao_botao_fatorial(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn3.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

btn4 = criar_botao(frame_botoes,"Fibonacci",lambda: acao_botao_fibonacci(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn4.grid(row=0,column=4, padx=5, pady=5,sticky="ew")

btn5 = criar_botao( frame_botoes, "Estruturas", lambda: acao_botao_estruturas(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn5.grid(row=0,column=5,padx=5,pady=5, sticky="ew")

btn6 = criar_botao(frame_botoes,"Ordenação",lambda: acao_botao_ordenacao(root, frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes))
btn6.grid(row=0,column=6,padx=5, pady=5, sticky="ew")

mostrar_menu_formatado(frame_tabela, frame_grafico_tempo, frame_grafico_iteracoes)

root.mainloop()