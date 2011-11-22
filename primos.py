# coding=utf-8
'''
Created on 31/10/2011

Testado em python 2.6

Gera os numeros primos ate o limit dado.

@author: Geraldo
'''

def fast_primes(limit=34000):
    if limit < 2:
        return []
    elif limit == 2:
        return [2]
    map = list(range(3, limit+1, 2))
    parada = limit**0.5
    atual = inicio = 3
    while atual <= parada:
        proximo = limit/atual
        while inicio <= proximo:
            indice = int((atual*inicio-3)/2)
            map[indice] = 0
            inicio += 2
        inicio = atual + 2
        atual += 2
    return [2] + [x for x in map if x]

if __name__ == '__main__':
    with open("lista_primos.txt", "w") as f:
        lista = fast_primes()
        for i in lista:
            f.write(str(i)+" ")
        print lista
    
    
    
