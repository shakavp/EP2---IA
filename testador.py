# coding=utf-8
import pylab
import os
import random
import burro

NUM_TESTES=200 # o certo é 200

'''
Created on 31/10/2011

Testado em python 2.6

TODO

@author: Geraldo
'''

def get_aleatorio(tamanho):
    numero = '1'
    for i in xrange(1, tamanho-1):
        bit = str(random.randint(0,1))
        numero = numero + bit
    numero = numero + '1'
    return numero
    
def produz_teste(tamanho):
    teste = []
    for i in xrange(NUM_TESTES): 
        teste.append(get_aleatorio(tamanho))
    return teste

def faz_graficos(x_list, y_list, x_label, y_label, save):
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.grid(True)
    pylab.plot(x_list, y_list)
    pylab.savefig(save)

if __name__ == '__main__':
    tamanhos = (5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)#o correto eh (15,20,25,30,35,40,45,50)
    respostas = []
    x_list1 = list(tamanhos)
    y_list1 = []
    x_list2 = list(tamanhos)
    y_list2 = []
    for tamanho in tamanhos:
        tempo_inicio = os.times()[0]
        #print tempo_inicio
        teste = produz_teste(tamanho)
        res = []
        tempos = []
        fatores_primos = 0
        for numero in teste:
            fat = burro.fatoracao_burra(numero)
            res.append(fat)
            tempo_teste = os.times()[0] - tempo_inicio
            tempo_inicio = os.times()[0]
            tempos.append(tempo_teste)
            fatores_primos = fatores_primos + len(fat)      
        y_list1.append(sum(tempos)/NUM_TESTES)
        y_list2.append((1.0*fatores_primos)/NUM_TESTES)

    print x_list1
    print y_list1
    faz_graficos(x_list1, y_list1, "m", "Tempo Medio", "1")

    print x_list2
    print y_list2
    faz_graficos(x_list2, y_list2, "m", "Numero Medio de Fatores Primos", "2")









#        print tamanho
#        print [int(i, 2) for i in teste]
#        print tempos
#        print "soma dos tempos", sum(tempos)
#        print "media dos tempos", sum(tempos)/NUM_TESTES
#        print res
#        print
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
