# Operadores aritméticos 2

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Adição
a = n1 + n2

# Subtração
s = n1 - n2

# Multiplicação
m = n1 * n2

# Divisão
d = n1 / n2

# Divisão inteira
di = n1 // n2

# Módulo
mod = n1 % n2

# Exponenciação
e = n1 ** n2

print("A adição é {}, a subtração é {}".format(a, s), end=" ")
print("e a multiplicação é {}".format(m))
print("A divisão é {:.3f}, a divisão inteira é {}, o modulo é {} e a exponenciação é {}".format(d, di, mod, e))
