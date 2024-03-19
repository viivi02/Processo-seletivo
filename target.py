"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);
"""
indice = 13
soma = 0
k = 0
while (k < indice):
    k += 1
    soma = soma + k
print(soma)
# Ao final do processamento, qual será o valor da variável SOMA?
# o valor da variável soma será de (91)

"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo 
valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na 
linguagem que desejar onde, informado um número, ele calcule a sequência 
de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.
"""

num = int (input('Informe o número a ser verificado: '))
a = 0
b = 1
c = 0
while (c < num):
    c = a + b
    a = b
    b = c 
if (c == num):
    print(f'O número {num} pertence a sequência de Fibonacci')
else:
    print(f'O número {num} não pertence a sequência de Fibonacci')
# O código ira verificar se o numero informado atraves do input pertence ou não a sequência

