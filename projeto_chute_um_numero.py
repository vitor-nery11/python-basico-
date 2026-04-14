"""
Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 10 e permita
que o usuário chute números até acertar o valor gerado.

O programa deve informar se o chute foi maior, menor ou igual ao valor aleatório
gerado no início.
"""

# Metodo dos 5Qs para montar um algoritmo

"""
1. quais são os dados de entrada necessarios?
-  valores inseridos pelo usuario

2. O que devo fazer com estes dados?
 - comparar com o valor que foi gerado de forma aleatoria
- validar se é o mesmo valor

 3. Quais são as restrições do problema?
 - Preciso dos valores inseridos pelo usuario 

4. Qual o resultado esperado?
 - acertar o valor aleatorio 
 - exibir o acerto depois

 5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
(PESEUDOCODIGO)

- recebo os valores inseridos pelo usuario
- vou comparando com o valor aleatorio gerado pelo codigo
- valido de se esta correto
- exibo o acerto
- finalizo o codigo "parabens, você acertou!"

"""

import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
   chute_usuario = int(input("Chute um numero:"))
   if chute_usuario > valor_aleatorio:
      print("chute um valor mais baixo")
   elif chute_usuario < valor_aleatorio:
      print("chute um valor mais alto")
   else:
      print("você acertou!")
      acertou = True 




