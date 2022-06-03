#Tipos embutidos (built-ins) e variáveis
#Exercício para conhecer os tipos de variáveis
var1 = "Hello World" #se usa aspas para indicar um texto
print(var1)
print("É uma variável do tipo", type(var1),"\n") #str é abreviação para string

var2 = 10 #é um numero inteiro
print(var2)
print("É uma variável do tipo", type(var2),"\n") #int abreviação para integer

var3 = 4.7 #é um numero fracionado ou ponto flutuante. Lembrar de usar ponto e não virgula.
print(var3)
print("É uma variável do tipo", type(var3),"\n") #float abreviação para floating point

var4 = 2 + 3j #é um numero complexo/imaginário (real + imag j)
print(var4)
print("É uma variável do tipo", type(var4),"\n") #complex abreviação para complex number
