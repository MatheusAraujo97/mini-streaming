import menu_usuario
import menu_filme

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
