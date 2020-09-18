"""
  Busca Binária Recursiva
    Entrada: 
        numeros: array numeros em ordem crescente
        n: Quantidade de numeros no array
        procurado: numero procurado
    Saida:
        Posição do numero no array
    Pseudocódigo:
    busca_binaria_recursiva(numeros,esquerda,direita,procurado)
        se esquerda > direita
            return NOT_FOUND
        senão
            meio = (esquerda+direita)/2
            se numeros[meio]== procurado
                return meio
            senao
                se numeros[meio] > procurado
                    return busca_binária_recursiva(numeros,esquerda,meio-1,procurado)
                senao
                    return busca_binária_recursiva(numeros,meio+1,direita,procurado)

"""
import math
def busca_binaria_recursiva(numeros,esquerda,direita,procurado):
    if esquerda > direita:
        return -1
    else:
        meio = math.floor((esquerda+direita)/2)
        if numeros[meio]==procurado:
            return meio
        else:
            if numeros[meio] > procurado:
                return busca_binaria_recursiva(numeros,esquerda,meio-1,procurado)
            else:
                return busca_binaria_recursiva(numeros,meio+1,direita,procurado)

numeros = [3,7,10,15,20]    
n = 5
procurado = 20
resposta = busca_binaria_recursiva(numeros,0,n-1,procurado)
print (resposta)
