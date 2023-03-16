from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('====================')
    print('=== Bem-vindo(a) ===')
    print('==== Mercadinho ====')
    print('====================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit()
    else:
        print('Opção inválida.')
        menu()

def cadastrar_produto() -> None:
    pass


def listar_produto() -> None:
    pass


def comprar_produto() -> None:
    pass


def visualizar_carrinho() -> None:
    pass


def fechar_pedido() -> None:
    pass


def pega_produto_por_codigo(codigo: int) -> Produto:
    pass


if __name__ == '__main__':
    main()
