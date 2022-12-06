#calculando o imc
from math import pow
peso = float(input(" Digite o peso em kg: "))
Altura = float(input(" Digite a estatura em metros: "))
idade = float(input(" Idade: "))
imc = peso/pow(Altura, 2)
print("O IMC é : {:.2f} ".format(imc))
if idade >= 65 and imc<= 18.49:
    print(" Classificação nutrcional: Idoso Baixo peso ")
elif idade >=65 and imc>= 18.5 and imc<= 24.99:
    print(" Classificação nutrcional: Idoso com peso Adequado ")
elif idade >= 65 and imc>= 25 and imc<=29.99:
    print(" Classificação nutrcional: Idoso Sobrepeso ")
elif idade >= 65 and imc>= 30:
    print(" Classificação nutrcional: Idoso com Obesidade ")
elif idade < 65 and imc<= 18.5:
    print(" Classificação nutrcional: Adulto Abaixo do peso ")
elif idade < 65 and imc>=18.5 and imc <=24.9:
    print(" Classificação nutrcional:Adulto em Peso Adequado ")
elif idade < 65 and imc> 24.9 and imc <=29.9:
    print(" Classificação nutrcional: Adulto Sobrepeso ")
elif idade < 65 and imc>= 30 and imc <= 34.9:
    print(" Classificação nutrcional: Adulto com Obesidade Grau I ")
elif idade < 65 and imc>= 35 and imc <= 39.9:
    print(" Classificação nutrcional: Adulto com Obesidade Grau II ")
elif idade < 65 and imc>= 40:
    print(" Classificação nutrcional:Adulto com Obesidade Grau III ")