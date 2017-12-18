import usuario

def menu_adicionar():
    cpf_usu = input("Digite o CPF: ")
    nome_usu = input("Digite seu nome: ")
    email_usu = input("Digite seu email: ")
    senha_usu = input("Senha: ")
    usuario.adicionar_usuario(cpf_usu, nome_usu, email_usu, senha_usu)

def menu_listar():
    lista_usuarios_adicionados = usuario.listar_usuarios()
    for u in lista_usuarios_adicionados:
        print(u)

def menu_buscar():
    cpf_usu = input("CPF:")
    u = usuario.buscar_usuario(cpf_usu)
    if (u == None):
        print("Usuário não encontrado!")
    else:
        print(u)

def menu_remover():
    cpf_usu = input("CPF: ")
    u = usuario.remover_usuario(cpf_usu)
    if (u == None):
        print("Usuário não encontrado!")
    else:
        print("Usuário removido!")

def mostrar_menu():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar Usuário \n" +
             "(2) Listar Usuários \n" +
             "(3) Buscar Usuário por CPF \n" +
             "(4) Remover Usuário \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_usuario):
        print(menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_usuario = False
        
