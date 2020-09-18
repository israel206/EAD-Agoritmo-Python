"""
    QuickSort(A,inicio,fim)
    Entrada:
         A: um vetor
         n: numero de elementos do vetor
    Resultado:
        Vetor de A ordenado
    Pseudocódigo:
        se inicio>=fim
            return
        senao
            pivo =Partition(A,inicio,fim)
            Quicksort(A,inicio,pivo-1)
            Quicksort(A,pivo+1,fim)
    
    Partition(A,inicio,fim)
    Entrada:
         A: um vetor
         n: numero de elementos do vetor
    Resultado:
        rearranja A[inicio...fim] para que A[inicio...pivo-1] < A[pivo] < A[pivo+1...fim] 
        retorna pivo
    Pseudocódigo:
        q = inicio
        para u = inicio até fim
            Se A[u] <=A[fim] 
                troque A[q] = A[u]
                q = q+1
        troque A[q] por A[fim]
        return q
"""
def Partition(A,inicio,fim):
    q = inicio
    for u in range(inicio,fim):
        if A[u] <=A[fim]:
            temp = A[q]
            A[q] = A[u]
            A[u] = temp
            q +=1
    temp = A[q]
    A[q] = A[fim]
    A[fim] = temp
    return q
def QuickSort(A,inicio,fim):
    if inicio>=fim:
        return
    else:
        pivo =Partition(A,inicio,fim)
        QuickSort(A,inicio,pivo-1)
        QuickSort(A,pivo+1,fim)
    return A

A = [12,7,14,9,11]
n = len(A)
resposta = QuickSort(A,0,n-1) 
print (resposta)




