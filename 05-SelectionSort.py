"""
    Selection sort(Ordenação por seleção)
    Entrada:
         A: um vetor
         n: numero de elementos do vetor
    Resultado:
        Vetor de A ordenado
    Pseudocódigo:
        Para i=1 até n-1
            menor = i
            Para j = i+1 até n
                Se A[j] < A[menor]
                    menor = j
            troca A[i] com A[menor]
    Complexidade:
             O(n^2) comparações
             O(n)   trocas
"""
def selection_sort(A,n):
    for i in range(0,n-1):
        menor = i
        for j in range(i+1,n):
            if A[j] < A[menor]:
                menor = j
        temp = A[menor]
        A[menor] = A[i]
        A[i] = temp
    return A

A = [1,5,6,4,2,7,3,10,25,12,15]
n = len(A)
resposta = selection_sort(A,n) 
print (resposta)

