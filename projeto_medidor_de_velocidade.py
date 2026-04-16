# Metodo dos 5Qs para montar um algoritmo

"""
1. quais são os dados de entrada necessarios?
2. O que devo fazer com estes dados
3. Quais são as restrições do problema?
4. Qual o resultado esperado?
 5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
(PESEUDOCODIGO)
"""
"""
Crie um programa que receba do usuário um valor que represente a velocidade em
uma via cuja velocidade máxima permitida é de 80 km/h.

Com base nesse valor, o programa deve informar se o motorista levou
uma multa leve, grave ou gravíssima.

Se a velocidade estiver abaixo ou igual a 80 km/h, exiba: "não houve multa".
Se estiver até 10 km/h acima, exiba: "levou multa leve".
Se estiver entre 11 km/h e 20 km/h acima, exiba: "levou multa grave".
Se estiver acima de 20 km/h, exiba: "levou multa gravíssima".

"""

velocidade = float(input("Digite a velocidade em que voccê estava:"))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print("Não houve multa!")
elif velocidade <= velocidade_maxima + 10:
    print("Levou multa leve")
elif velocidade <= velocidade_maxima + 20:
    print("Levou multa grave")
else:
    print("Multa gravíssima")
