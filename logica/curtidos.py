from logica import filme

filmes_curtidos = []

def adicionar_filme_curtido(cod_filme):
    for f in filme.filmes:
        if f[0] == cod_filme:
            filmes_curtidos.append(f)
    return None

def listar_filmes_curtidos():
    return filmes_curtidos
