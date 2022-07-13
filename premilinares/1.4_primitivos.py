# Tipos primitivos

n1 = input("Digite o primeiro valor: ")
n2 = input("Digite o segundo valor: ")

n3 = n1 + n2

print("\nA soma de {} e {} é {}".format(n1, n2, n3))
print("tipo de n1 é %s" % type(n1))
print("tipo de n2 é %s" % type(n2))
print("tipo de n3 é %s" % type(n3))
print("*"*30)

# Conversão de str em int
n1_int = int(n1)
n2_int = int(n2)

n3 = n1_int + n2_int

print("\nA soma de {} e {} é {}".format(n1_int, n2_int, n3))
print("tipo de n1 é %s" % type(n1_int))
print("tipo de n2 é %s" % type(n2_int))
print("tipo de n3 é %s" % type(n3))
print("*"*30)


# Conversão de n1 em float e n2 em int
n1_float = float(n1)

n3 = n1_float + n2_int

print("\nA soma de {} e {} é {}".format(n1_float, n2_int, n3))
print("tipo de n1 é %s" % type(n1_float))
print("tipo de n2 é %s" % type(n2_int))
print("tipo de n3 é %s" % type(n3))
print("*"*30)