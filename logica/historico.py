from logica import filme

filmes_assistidos = []

def adicionar_filme_assistido(cod_filme):
    for f in filme.filmes:
        if f[0] == cod_filme:
            filmes_assistidos.append(f)
    return None

def listar_filmes_assistidos():
    return filmes_assistidos
