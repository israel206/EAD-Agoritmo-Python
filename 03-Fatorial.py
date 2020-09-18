"""
    03-Fatorial Recursivo
    
    Entrada: n>=0
    Saida:  valor de n!
    Pseudo Código:
        se n=0 retorna 1
        senão retorna n*(n-1)!
    
    Complexidade O(n)
"""
def fatorial(n):
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)

n = 3
resposta = fatorial(n)
print (resposta)
