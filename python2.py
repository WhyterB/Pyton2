import os

restaurantes = [
    {"nome": "Bife-Sujo", "categoria": "Prato Feito", "ativo": True},
    {"nome": "Saco-de-Feijão", "categoria": "Feijoada", "ativo": False},
    {"nome": "Carlesso-Porquinhos-Assados", "categoria": "Assados", "ativo": True}
]


def limpar_tela():
    os.system('clear')


def mostrar_subtitulo(texto=""):
    limpar_tela()
    print(texto + "\n")


def finalizar_app():
    mostrar_subtitulo("Finalizando o app")
    exit()


def chamar_nome_do_app():
    print('''
    
░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ ░█─░█ ░█▀▀█ ─█▀▀█ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀ 　 ░█▀▀▀ ▀▄░▄▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀█ 
░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ─░█── ░█▄▄█ ░█─░█ ░█▄▄▀ ░█▄▄█ ░█░█░█ ─░█── ░█▀▀▀ 　 ░█▀▀▀ ─░█── ░█▄▄█ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ─▀▀▀▄▄ ░█──░█ 
░█─░█ ░█▄▄▄ ░█▄▄▄█ ─░█── ░█─░█ ─▀▄▄▀ ░█─░█ ░█─░█ ░█──▀█ ─░█── ░█▄▄▄ 　 ░█▄▄▄ ▄▀░▀▄ ░█─── ░█─░█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄█

    
    ''')


def voltar_ao_menu_principal():
    input('\nPressione Enter para voltar ao menu principal')
    main()


def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alternar Estado do Restaurante")
    print("4. Sair\n")


def cadastrar_novo_restaurante():
    mostrar_subtitulo("Cadastro de Novo Restaurante")
    nome_do_restaurante = input('Digite o nome do novo restaurante: ')
    categoria_do_restaurante = input('Digite a categoria do restaurante: ')
    ativo_do_restaurante = input('O restaurante está ativo? (S/N): ').upper() == 'S'
    restaurantes.append({"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo": ativo_do_restaurante})
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    mostrar_subtitulo('Listando os Restaurantes')
    for restaurante in restaurantes:
        status = "Ativo" if restaurante["ativo"] else "Inativo"
        print(f"- {restaurante['nome']} | Categoria: {restaurante['categoria']} | Status: {status}")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    mostrar_subtitulo("Alternar o estado do restaurante")
    nome_restaurante = input("Digite o nome do Restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True
            break
    if restaurante_encontrado:
        print(f'O estado do restaurante "{nome_restaurante}" foi alterado com sucesso.')
    else:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_digitada = int(input("Escolha uma opção: "))
        print("Você selecionou:", opcao_digitada, "\n")
        if opcao_digitada == 1:
            cadastrar_novo_restaurante()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            alternar_estado_restaurante()
        elif opcao_digitada == 4:
            print('Você escolheu sair do programa')
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    limpar_tela()
    chamar_nome_do_app()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
