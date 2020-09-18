"""
Busca Linear - Procurando livros em biblioteca desorganizada
   Entrada: 
            livros:     arranjo
            qtd_livros: numero de elementos do arranjo
            procurado:  valor que buscamos
    Saída: 
        um índice com a posição de procurado(2) ou NOT_FOUND(-1)
    PSEUDO-CÓDIGO:
        resposta = NOT_FOUND
        para cada i indo de 1ª a qtd_livros em ordem:
            se livros[i]== procurado então resposta=i
        return resposta
    Complexidade:
        O(n) tempo
        pior caso 
"""
#def busca_linear(livros,qtd_livros,procurado):
#    resposta = -1
def busca_linear(livros,qtd_livros,procurado):
    retorno = -1
    for i in range(qtd_livros):
        if livros[i] == procurado:
            retorno = i
    return retorno        

livros = ['shakespeare','machado de assis','lima barreto','charles dickens']
qtd_livros = 4
procurado = 'shakespeare'
resposta = busca_linear(livros,qtd_livros,procurado)
print(resposta)
