import json 
import random
# Este programa é um sistema simples de gerenciamento de estoque para uma empresa. Ele permite adicionar produtos, remover produtos e visualizar o estoque atual. Cada produto tem um nome, quantidade, valor e um código gerado aleatoriamente.

print("Bem Vindo ao Fluxo de Estoque!   ")
print("Vamos começar a organizar o estoque da sua empresa!   ")
# O programa utiliza um dicionário para armazenar os produtos, onde a chave é o nome do produto e o valor é outro dicionário contendo a quantidade, valor e código do produto. O menu de opções é exibido em um loop, permitindo que o usuário escolha entre as diferentes funcionalidades até decidir sair do programa.
produtos = {}

# A função `menu()` exibe as opções disponíveis para o usuário e retorna a escolha feita. As funções `adicionar_produto()`, `remover_produto()` e `ver_estoque()` implementam as funcionalidades correspondentes para gerenciar o estoque. O programa é iniciado pela função `main()`, que controla o fluxo principal do programa. 
def menu()  :
    print("\nMenu de Opções:")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Ver Estoque")
    print("4. Sair")    
    return input("Escolha uma opção: ")

# A função `adicionar_produto()` solicita ao usuário o nome, quantidade e valor do produto, gera um código aleatório para o produto e adiciona as informações ao dicionário de produtos. A função `remover_produto()` permite ao usuário remover uma quantidade específica de um produto existente no estoque, verificando se a quantidade solicitada é menor ou igual à quantidade disponível. A função `ver_estoque()` exibe o estoque atual, mostrando o nome do produto, a quantidade disponível, o valor unitário e o código do produto. O programa continua executando até que o usuário escolha a opção de sair.
def adicionar_produto():
    
    nome = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        if quantidade < 0:
            print("Quantidade não pode ser negativa.")
            return
        
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return
    try:
        valor = float(input("Digite o valor do produto: "))
        if valor < 0:
            print("Valor não pode ser negativo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor válido.")
        return
    codigo_do_produto = random.randint(1000, 9999)
    print(f"Código do produto: {codigo_do_produto}")   
    produtos[nome] = {'quantidade': produtos.get(nome, {}).get('quantidade', 0) + quantidade, 'valor': valor, 'codigo': codigo_do_produto }
    print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")

# A função `adicionar_produto()` solicita ao usuário o nome, quantidade e valor do produto, gera um código aleatório para o produto e adiciona as informações ao dicionário de produtos. A função `remover_produto()` permite ao usuário remover uma quantidade específica de um produto existente no estoque, verificando se a quantidade solicitada é menor ou igual à quantidade disponível. A função `ver_estoque()` exibe o estoque atual, mostrando o nome do produto, a quantidade disponível, o valor unitário e o código do produto. O programa continua executando até que o usuário escolha a opção de sair.
def remover_produto():
    nome = input("Digite o nome do produto a remover: ")
    if nome in produtos:
        try:
            quantidade = int(input("Digite a quantidade a remover: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
                return
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            return
        if quantidade <= produtos[nome]['quantidade']:
            produtos[nome]['quantidade'] -= quantidade
            print(f"{quantidade} unidades de {nome} removidas do estoque.")
            if produtos[nome]['quantidade'] == 0:
                del produtos[nome]
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não encontrado no estoque.")

 # A função `adicionar_produto()` solicita ao usuário o nome, quantidade e valor do produto, gera um código aleatório para o produto e adiciona as informações ao dicionário de produtos. A função `remover_produto()` permite ao usuário remover uma quantidade específica de um produto existente no estoque, verificando se a quantidade solicitada é menor ou igual à quantidade disponível. A função `ver_estoque()` exibe o estoque atual, mostrando o nome do produto, a quantidade disponível, o valor unitário e o código do produto. O programa continua executando até que o usuário escolha a opção de sair.       
def ver_estoque():
    if produtos:
        print("\nEstoque Atual:")                                       
        for nome, info in produtos.items():
            print(f"{nome}: {info['quantidade']} unidades (R$ {info['valor']:.2f} cada) - Código: {info.get('codigo', 'N/A')}")
    else:
        print("O estoque está vazio.")

def salvar_estoque():
    with open('estoque.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)
    print("Estoque salvo com sucesso.")

def carregar_estoque():
    try:
        with open('estoque.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def main():
    global produtos
    produtos = carregar_estoque()
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            ver_estoque()
        elif opcao == '4':
            salvar_estoque()
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
if __name__ == "__main__":
        main()  
   


