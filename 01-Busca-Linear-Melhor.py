"""
Busca Linear Melhor - Procurando livros em biblioteca desorganizada
   Entrada: 
            livros:     arranjo
            qtd_livros: numero de elementos do arranjo
            procurado:  valor que buscamos
    Saída: 
        um índice com a posição de procurado ou NOT_FOUND
    PSEUDO-CÓDIGO:
        para i=1 até n:
            se livros[i]==procurado return i
        return NOT_FOUND     
    Complexidade:
        O(n) em tempo
"""
def busca_linear_melhor(livros,qtd_livros,procurado):
    for i in range(qtd_livros):
        if livros[i]==procurado:
        return i
    return -1    
    
livros = ['shakespeare','machado de assis','lima barreto','charles dickens']
qtd_livros = 4
procurado = 'charles dickens'
resposta = busca_linear_melhor(livros,qtd_livros,procurado)
print(resposta)
