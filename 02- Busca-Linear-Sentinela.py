"""
Busca Linear com Sentinela - Procurando livros em biblioteca desorganizada
   Entrada: 
            livros:     arranjo
            n: numero de elementos do arranjo
            procurado:  valor que buscamos
    Saída: 
        um índice com a posição de procurado ou NOT_FOUND
    PSEUDO-CÓDIGO:
        salve livros[n]   
        atribua procurado em livros[n]
        i=1
        Enquanto livros[i]!=procurado
            i++
        Restaura livros[n] de ultimo
        se i<n ou livros[n]==procurado return i
        senao return NOT_FOUND  
    Complexidade:
        O(n) em tempo
"""
def busca_linear_sentinela(livros,n,procurado):
    ultimo = livros[n-1]
    livros[n-1] = procurado
    i=0
    while livros[i]!=procurado:
        i+=1
    livros[n-1] = ultimo
    if i<n-1 or livros[n-1]==procurado:
        return i
    else:
        return -1   
        
livros = ['shakespeare','julio verne','lima barreto','machado de assis','charles dickens']        
n = 5
procurado = 'lima barreto'
resultado = busca_linear_sentinela(livros,n,procurado)
if resultado == -1:
    print('NOT FOUND')
else:
    print(resultado)    
