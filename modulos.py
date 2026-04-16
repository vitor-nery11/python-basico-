print("exemplo de importação de um modulo padrão")
#importa a biblioteca completa 
import math 
# importa somente o necessario 
from math import sqrt

raiz_quadrada = math.sqrt(25)
print(f"a raiz quadrada de 25 é {raiz_quadrada}")

print("\n Exemplo de criação e utilização de um modulo personlizado")
import meu_modulo

mensagem = meu_modulo.Saudacao("vitor")
resultado_dobro = meu_modulo.dobro(5)

print(mensagem)
print(f"o dobro de 5 é {resultado_dobro}")