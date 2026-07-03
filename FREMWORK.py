import tkinter as tk

# ---------------- JANELA ----------------

janela = tk.Tk()
janela.title("Controle de Estoque")
janela.geometry("700x500")
janela.resizable(False, False)

# ---------------- FUNÇÕES ----------------

def adicionar():
    print("Adicionar Produto")

def remover():
    print("Remover Produto")

def consultar():
    print("Consultar Produto")

def estoque():
    print("Ver Estoque")

def editar():
    print("Editar Produto")

def total():
    print("Valor Total")

# ---------------- TÍTULO ----------------

titulo = tk.Label(
    janela,
    text="CONTROLE DE ESTOQUE",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=30)

# ---------------- BOTÕES ----------------

btn1 = tk.Button(
    janela,
    text="➕ Adicionar Produto",
    width=30,
    height=2,
    command=adicionar
)
btn1.pack(pady=5)

btn2 = tk.Button(
    janela,
    text="➖ Remover Produto",
    width=30,
    height=2,
    command=remover
)
btn2.pack(pady=5)

btn3 = tk.Button(
    janela,
    text="🔍 Consultar Produto",
    width=30,
    height=2,
    command=consultar
)
btn3.pack(pady=5)

btn4 = tk.Button(
    janela,
    text="📋 Ver Estoque",
    width=30,
    height=2,
    command=estoque
)
btn4.pack(pady=5)

btn5 = tk.Button(
    janela,
    text="💰 Valor Total",
    width=30,
    height=2,
    command=total
)
btn5.pack(pady=5)

btn6 = tk.Button(
    janela,
    text="✏ Editar Produto",
    width=30,
    height=2,
    command=editar
)
btn6.pack(pady=5)

btn7 = tk.Button(
    janela,
    text="🚪 Sair",
    width=30,
    height=2,
    command=janela.destroy
)
btn7.pack(pady=20)

janela.mainloop()
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()


def menu_principal():
    limpar_tela()

    titulo = tk.Label(
        janela,
        text="CONTROLE DE ESTOQUE",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    tk.Button(janela, text="➕ Adicionar Produto", width=30, height=2,
              command=tela_adicionar).pack(pady=5)

    tk.Button(janela, text="➖ Remover Produto", width=30, height=2,
              command=lambda: print("Remover")).pack(pady=5)

    tk.Button(janela, text="🔍 Consultar Produto", width=30, height=2,
              command=lambda: print("Consultar")).pack(pady=5)

    tk.Button(janela, text="📋 Ver Estoque", width=30, height=2,
              command=lambda: print("Estoque")).pack(pady=5)

    tk.Button(janela, text="💰 Valor Total", width=30, height=2,
              command=lambda: print("Valor Total")).pack(pady=5)

    tk.Button(janela, text="✏ Editar Produto", width=30, height=2,
              command=lambda: print("Editar")).pack(pady=5)

    tk.Button(janela, text="🚪 Sair", width=30, height=2,
              command=janela.destroy).pack(pady=20)


def tela_adicionar():
    limpar_tela()

    tk.Label(
        janela,
        text="ADICIONAR PRODUTO",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(janela, text="Nome do Produto").pack()

    entrada_nome = tk.Entry(janela, width=40)
    entrada_nome.pack(pady=5)

    tk.Label(janela, text="Quantidade").pack()

    entrada_quantidade = tk.Entry(janela, width=40)
    entrada_quantidade.pack(pady=5)

    tk.Label(janela, text="Valor").pack()

    entrada_valor = tk.Entry(janela, width=40)
    entrada_valor.pack(pady=5)

    def salvar():
        nome = entrada_nome.get()
        quantidade = entrada_quantidade.get()
        valor = entrada_valor.get()

        print(nome)
        print(quantidade)
        print(valor)

    tk.Button(
        janela,
        text="Salvar",
        width=20,
        command=salvar
    ).pack(pady=15)

    tk.Button(
        janela,
        text="Voltar",
        width=20,
        command=menu_principal
    ).pack()
    