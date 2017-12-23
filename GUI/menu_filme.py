from logica import filme
from logica import historico
from logica import curtidos

cont = 0
def gerar_codigo():
    global cont
    cont += 1
    return cont

def imprimir_filme(f):
    print("Código:", f[0])
    print("Título:", f[1])
    print("Genêro:", f[2])
    print("Ano:", f[3])
    print("")

def menu_adicionar():
    cod = gerar_codigo()
    titulo_filme = input("Título  do filme: ")
    genero_filme = input("Genêro: ")
    ano_filme = input("Ano: ")
    for f in filme.listar_filmes():
        if titulo_filme == f[1]:
            print("Esse filme já foi adicionado!")
            return None
    filme.adicionar_filmes(cod, titulo_filme, genero_filme, ano_filme)

def menu_listar():
    lista_filmes = filme.listar_filmes()
    for f in lista_filmes:
        imprimir_filme(f)

def menu_buscar():
    cod = int(input("Digite o código do filme: "))
    f = filme.buscar_filme(cod)
    if (f == None):
        print("Filme não encontrado!")
    else:
        print(f)
        historico.adicionar_filme_assistido(cod)
        print("(1) Curtir")
        print("(0) Sair")
        opcao = input("Digite o código conforme escolha")
        if opcao == "1":
            curtidos.adicionar_filme_curtido(cod)

def menu_historico():
    filmes_no_historico = historico.listar_filmes_assistidos()
    for f in filmes_no_historico:
        imprimir_filme(f)

def menu_curtidos():
    filmes_curtidos = curtidos.listar_filmes_curtidos()
    for f in filmes_curtidos:
        imprimir_filme(f)

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
             "(6) Histórico \n" +
             "(7) Filmes curtidos \n" +
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
        elif op == "6":
            menu_historico()
        elif op == "7":
            menu_curtidos()
        elif op == "0":
            run_menu = False
             
     
