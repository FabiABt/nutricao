#calculando o imc
from math import pow
peso = float(input(" Digite o peso em kg: "))
Altura = float(input(" Digite a estatura em metros: "))
idade = input(" Idade: ")
imc = peso/pow(Altura, 2)
print(imc)