import random

print("Bem Vindo ao Fluxo de Estoque!   ")
print("Vamos começar a organizar o estoque da sua empresa!   ")

produtos = {}
 
def menu()  :
    print("\nMenu de Opções:")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Ver Estoque")
    print("4. Sair")    
    return input("Escolha uma opção: ")

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor = float(input("Digite o valor do produto: "))
    codigo_do_produto = random.randint(1000, 9999)
    print(f"Código do produto: {codigo_do_produto}")   
    produtos[nome] = {'quantidade': produtos.get(nome, {}).get('quantidade', 0) + quantidade, 'valor': valor, 'codigo': codigo_do_produto         }
    print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")  

def remover_produto():
    nome = input("Digite o nome do produto a remover: ")
    if nome in produtos:
        quantidade = int(input("Digite a quantidade a remover: "))
        if quantidade <= produtos[nome]['quantidade']:
            produtos[nome]['quantidade'] -= quantidade
            print(f"{quantidade} unidades de {nome} removidas do estoque.")
            if produtos[nome]['quantidade'] == 0:
                del produtos[nome]
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não encontrado no estoque.")
def ver_estoque():
    if produtos:
        print("\nEstoque Atual:")                                       
        for nome, info in produtos.items():
            print(f"{nome}: {info['quantidade']} unidades (R$ {info['valor']:.2f} cada) - Código: {info.get('codigo', 'N/A')}")
    else:
        print("O estoque está vazio.")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            ver_estoque()
        elif opcao == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
if __name__ == "__main__":
    main()  

   


