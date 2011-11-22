# coding=utf-8
import burro

'''
Created on 31/10/2011

Testado em python 2.6

Interface que dado um numero em binario devolve seus fatores primos.
Espera-se que a entrada esteja correta.

@author: Geraldo
'''

def main():
    numero = raw_input("Digite um numero em binario:")
    lista = burro.fatoracao_burra(numero)
    colecao = list(set(lista))
    for i in colecao:
        num = str(bin(i))
        print num[2:], lista.count(i)
    
    #print de debug
    print lista

main()
