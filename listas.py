# Listas 
precos = [20, 50, 100]
print(precos[0]) # acessando por indice 

nomes = ["Brazil", "Suiça", "Afegaristão"]
print(nomes[1]) # acessando por indice 

# Encontrar indice automatico 
print(nomes.index("Suiça"))

# Manipular - add novos itens 
salarios = [2500, 5000, 7000]
salario_usuario = float(input("Qual é o seu salário?"))
salarios.append(salario_usuario)
print(salarios)

