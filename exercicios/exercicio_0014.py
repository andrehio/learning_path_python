# Exercício 14
# Escreva um programa que converta uma temperatura digitada em ºC e converta
# para ºF e K.

c = float(input("Informe a temperatura em ºC: "))
f = 9 * c / 5 + 32
k = c + 273.15
print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF e {:.1f}K"
      .format(c, f, k))
