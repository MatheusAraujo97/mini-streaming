usuarios = []

def adicionar_usuario(cpf, nome, email, senha):
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)

def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if u[0] == cpf:
            return u
        return None

def remover_usuario(cpf):
    for u in usuarios:
        if u[0] == cpf:
            usuarios.remove(u)
            return True

    
