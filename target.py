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

"""
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___
R: O próximo número será 9, a numeração esta subindo de 2 em 2.

b) 2, 4, 8, 16, 32, 64, ____
R:O próximo é 128, a sequência seria a elevação do numero 2 até 7.

c) 0, 1, 4, 9, 16, 25, 36, ____
R: 49, a lista é uma sequencia numerica de numeros elevados a 2 e parou no 7.

d) 4, 16, 36, 64, ____
R: O próximo é 100, a sequencia eo quadrado dos numeros pares.

e) 1, 1, 2, 3, 5, 8, ____
R: O próximo será 13, esta é a sequência de fibonacci.

f) 2,10, 12, 16, 17, 18, 19, ____
R: 200, todos tem D na inicial.
"""

"""
4) Você está em uma sala com três interruptores, cada um conectado a 
uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala
em que está, mas pode ligar e desligar os interruptores quantas vezes 
quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas
das lâmpadas, qual interruptor controla cada lâmpada?


"""

"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""