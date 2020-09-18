"""
Counting Sort
    Entradas:
        A: um vetor de inteiros na faixa de 0 a m-1
        n: o número de elementos em A
        m: define a faixa de valores em A
    Saida:
        Um vetor B que contém os elementos de A ordenados
    Pseudocódigo:
        equal = CountKeysEqual(A,n,m)
        less = CountKeysLess(equal,m)
        B = Rearrange(A,less,n,m)
        return B
Procedimento Count Keys Equal:
    Entrada: 
        A: um vetor de inteiros na faixa 0 a m-1
        n: numero de elementos em A
        m: define a faixa de valores em A
    Saida:
        Um vetor equal[0...m-1] onde equal[j] é a quantidade de elementos iguais a [j]
    Pseudocódigo:
        Declare equal[0...m-1]
        equal[0 até m-1] = 0
        for i=1 até n
            key = A[i] 
            incremente equal[key]
        return equal
Procedimento Count Keys Kess:
    Entrada:
        equal: o vetor retornado por Count Keys Equal
        m: a faixa de indices de equal: 0 a m-1
    Saida:
        UM vetor less[0...m-1] tal que j=0,1,...m-1, less contém a soma equal[0]+equal[1]...equal[j-1] 
    Pseudocódigo:
        declare less[0,m-1]
        less[0] = 0
        for j=1 a m-1
            less[j] = less[j-1]+equal[j-1]
        return less
Procedimento Rearrange:
    Entrada:
        A: um vetor de inteiros na faixa 0 a m-1
        less: o vetor retornado de count keys less
        n: o numero de elementos em A
        m: a faixa de valores em A
    Saida:
        um vetor B contendo os elementos de A ordenados
    Pseudocódigo:
        Seja B[1..n] e next[0..m-1] novos vetores
        para j=0 a m-1
            next[j] = less[j]+1
        para i =1 a n
            key =A[i]
            index = next[key]
            B[index] = A[i]
            next[key] +=1
        return B
"""
def Rearrange(A,less,n,m):
    B = [0]*n
    nextt = [0]*m
    for j in range(0,m):
        nextt[j] = less[j]+1
    print ("B=",B,"next=",nextt)
    for i in range(0,n):
        key = A[i]
        index = nextt[key]-1
        B[index] = A[i]
        nextt[key] +=1
        print ("B=",B,"next=",nextt)
    return B

def CountKeysLess(equal,m):
    less = [0]*m
    for i in range(0,m):
        less[i] = 0
    for j in range(1,m):
        less[j] = less[j-1]+equal[j-1]
    return less

def CountKeysEqual(A,n,m):
    equal = [0]*m
    for i in range(0,m):
        equal[i]=0
    for i in range(0,n):
        key = A[i]
        equal[key] +=1
    return equal

def CountingSort(A,n,m):
    equal = CountKeysEqual(A,n,m)
    less = CountKeysLess(equal,m)
    B = Rearrange(A,less,n,m)
    return B
A = [4,1,5,0,1,6,5,1,5,3]
n = len(A)
m = 7
resposta = CountingSort(A,n,m)
print (resposta)



