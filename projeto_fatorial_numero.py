# Metodo dos 5Qs para montar um algoritmo

"""
1. quais são os dados de entrada necessarios?
- numero a ser fatorado

2. O que devo fazer com estes dados?
 - multiplicar de forma descrescente por seus numeros antecessores até chegar no seu fatorial

 3. Quais são as restrições do problema?
 - Preciso de numero a ser fatorado

4. Qual o resultado esperado?
 - Exibir o fatorial do numero de entrada

 5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?
(PESEUDOCODIGO)

- recebo um valor que é o numero a descobrir o fatorial 
- verificar se é um numero positivo e inteiro
- multiplico esse valor por cada um dos antecessores dele até chegar a 1 
- exibir o resultado do fatorial desse numero

"""

number = int(input("Digite o numero a ser fatorado:"))
if number > 0 and  type(number) == int:
    fatorial = 1
    for item in range(1,number+1):
        fatorial = fatorial * item
        print(f"{fatorial} * {item} = {fatorial}")
    print(f"o fatorial de {number} é {fatorial}")
else:
    print("por favor informar apenas numeros inteiros positivos")


