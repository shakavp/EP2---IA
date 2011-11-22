# coding=utf-8
import primos

'''
Created on 31/10/2011

Testado em python 2.6

Faz pelo metodo da força bruta a fatoração do numero binario, que é
uma string de 1's e 0's.
Devolve uma lista de seus termos primos. 

@author: Geraldo
'''

def fatoracao_burra(binario):
    lista_primos = primos.fast_primes()
    numero = int(binario, 2)
    fatores = []
    for i in lista_primos:
        while numero % i == 0 and numero > 1:
            fatores.append(i)
            numero = numero / i
        if numero == 1:
            break
    return fatores
    
if __name__ == '__main__':
    binario = '111111111111111111111'
    atual = 1
    for i in fatoracao_burra(binario):
        atual = atual * i
    print int(binario, 2), len(binario), fatoracao_burra(binario)
    print atual
    if atual == int(binario, 2):
        print "OK"   
                    

