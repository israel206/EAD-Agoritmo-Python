"""
    Ordenação por inserção - Insertion Sort
    Entrada:
         A: um vetor
         n: numero de elementos do vetor
    Resultado:
        Vetor de A ordenado
    Pseudocódigo:
        para i=2 a n
            chave = A[i]
            j = i-1
            Enquanto j>0 e A[j] > chave
                A[j+1] = A[j]
                j = j-1
        A[j+1] = chave
        O(n^2) comparações
        O(n^2) trocas
"""
def insertion_sort(A,n):
    for i in range(1,n):
        chave = A[i]
        j = i-1
        while j>=0 and A[j] > chave:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = chave
    return A

A = [5,18,5,4,2,7,3,10,25,12,15]
n = len(A)
resposta = insertion_sort(A,n) 
print (resposta)

