"""
    Ordenação por Intercalação Merge Sort
    Entrada:
         A: um vetor
         n: numero de elementos do vetor
    Resultado:
        Vetor de A ordenado
    Pseucodódigo:
        se inicio>=fim
            return A
        senao
            meio = (inicio+fim)/2
            mergeSort(A,inicio,meio)
            mergeSort(A,meio+1,fim)
            Merge(A,esquerda,meio,direita) 

    
"""
"""
    Procedimento Merge
    Entrada:
        A: um vetor
        inicio,meio,fim: indices de A 
    Saida:
        Subvetor: A[inicio...fim] contem A[inicio...meio] e A[meio+1...fim] agora subvetor A[inicio...fim] ordenado
    Pseucódigo:
        n1 = meio-inicio+1
        n2 = fim-meio
        B[1...n1] = A[inicio...meio]
        C[1...n2] = A[meio+1...fim]
        B[n1+1] = infinito
        C[n2+1] = infinito
        i = 0
        j = 0
        para k = inicio a fim
            Se B[i]<=C[j]
                A[k]=B[i]
                i = i+1
            Senao
                A[k] = C[j]
                j = j+1

    complexidade:
        tempo: O(n *lg n) 
        trocas: O(n*lg n)
"""
import math
def Merge(A,inicio,meio,fim):
    n1 = meio-inicio +1
    n2 = fim-meio
    B = [0]* n1
    C = [0]* n2
    for i in range(0,n1):
        B[i] = A[inicio + i]
    for j in range(0,n2):
        C[j] = A[meio+1 +j]
    B.append(99999)
    C.append(99999)
    i = 0
    j = 0
    for k in range(inicio,fim+1):
        if B[i]<=C[j]:
            A[k]=B[i]
            i = i+1
        else:
            A[k] = C[j]
            j = j+1
    return 
    

def mergeSort(A,inicio,fim):
    if inicio>=fim:
        return 
    meio = math.floor((inicio+fim)/2)
    mergeSort(A,inicio,meio)
    mergeSort(A,meio+1,fim)
    Merge(A,inicio,meio,fim)
    return A
 
A = [5,6,2,2,15,6]
n = len(A)
resposta = mergeSort(A,0,n-1) 
print (resposta)
""" 
[6,5,4,3]
[6,5]
[6] [5]
i=0       j=2
[5,6,inf]   [3,4,inf]
k   =0
[3,4,5,6]

"""