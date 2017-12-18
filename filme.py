filmes = []

def adicionar_filmes(cod_filme, titulo, genero, ano):
    filme = [cod_filme, titulo, genero, ano]
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for f in filmes:
        if f[0] == cod_filme:
            return f
    return None

def buscar_filmes_por_genero(genero):
    for f in filmes:
        if f[2] == genero:
            return f
    return None

def remover_filme(cod_filme):
    for f in filmes:
        if f[0] == cod_filme:
            filmes.remove(f)
            return True


    
