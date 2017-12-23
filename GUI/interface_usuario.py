from GUI import menu_usuario
#from logica import usuario

from GUI import menu_filme
#from logica import filme
#from logica import curtidos
#from logica import historico

def menu_geral():
    run_menu_principal = True

    while run_menu_principal:
        print("(1) Menu Usuário")
        print("(2) Menu Filme")
        print("(0) Sair")

        op = input("Digite sua escolha:")

        if op == "1":
            menu_usuario.mostrar_menu()
        elif op == "2":
            menu_filme.mostrar_menu()
        elif op == "0":
            break
    
    print("Programa finalizado!")
