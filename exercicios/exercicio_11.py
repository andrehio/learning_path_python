# Exercício 11
# Crie um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 m².

l = float(input("Largura da parede (m): "))
a = float(input("Altura da parede (m): "))
area = l * a
print("Sua parede tem a dimensão de {} m x {} m e sua área é de {} m².".format(
    l, a, area))
print("Para pintar essa parede, você precisará de {} L de tinta.".format(area
                                                                       / 2))
