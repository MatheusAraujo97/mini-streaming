import filme

cont = 0
def gerar_codigo():
    global cont
    cont += 1
    return cont
    
def menu_adicionar():
    cod = gerar_codigo()
    titulo_filme = input("Título  do filme: ")
    genero_filme = input("Genêro: ")
    ano_filme = input("Ano: ")
    filme.adicionar_filmes(cod, titulo_filme, genero_filme, ano_filme)

def menu_listar():
    lista_filmes = filme.listar_filmes()
    for f in lista_filmes:
        print(f)

def menu_buscar():
    cod = int(input("Digite o código do filme: "))
    f = filme.buscar_filme(cod)
    if (f == None):
        print("Filme não encontrado!")
    else:
        print(f)

def menu_buscar_genero():
    genero_filme = input("Digite o genêro do filme: ")
    f = filme.buscar_filmes_por_genero(genero_filme)
    if (f == None):
        print("Genêro não encontrado!")
    else:
        print(f)

def menu_remover():
    cod = int(input("Digite o código do filme: "))
    f = filme.remover_filme(cod)
    if (f == None):
        print("Filme não encontrado!")
    else:
        print("Filme removido!")

def mostrar_menu():
    run_menu = True

    menu = ("\n----------------\n"+
             "(1) Adicionar Filme \n" +
             "(2) Listar Filmes \n" +
             "(3) Buscar Filme por código \n" +
             "(4) Buscar Filmes por genêro \n" +
             "(5) Remover Filme \n" +
             "(0) Voltar\n"+
            "----------------")

    while run_menu:
        print(menu)

        op = input("Digite a sua escolha: ")

        if op == "1":
            menu_adicionar()
        elif op == "2":
            menu_listar()
        elif op == "3":
            menu_buscar()
        elif op == "4":
            menu_buscar_genero()
        elif op == "5":
            menu_remover()
        elif op == "0":
            run_menu = False
             
     
