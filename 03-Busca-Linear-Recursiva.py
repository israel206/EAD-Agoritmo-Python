"""
    Busca Linear Recursiva
    Entrada: 
        livros: array livros
        n: numero de livros
        procurado: livro procurado
        i: iterador
    Saida:
        Posição do livro
    Pseudocódigo:
        Se i>n então retorna NOT_FOUND
        Senão 
            se livros[i]==procurado retorna i
            Senão retorna busca_linear_recursiva(livros,n,i+1,procurado)
    Complexidade:
        O(n)

"""
def busca_linear_recursiva(livros,n,i,procurado):
    if i>n:
        return -1
    else:
        if livros[i]==procurado: 
            return i
        else:
            return busca_linear_recursiva(livros,n,i+1,procurado)
livros = ['shakespeare','lima barreto','julio verne','machado de assis']    
n = 4
i=0
procurado = 'machado de assis' 
resposta = busca_linear_recursiva(livros,n,i,procurado)
print (resposta)

