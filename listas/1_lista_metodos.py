# Lista
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Exemplos de aplicação de métodos sobre listas
'''

nums = [17, 33, 8, 11, 8, 15, 9]
print("vetor: %s" % nums)
# adiciona o elemento 10 ao final da lista
nums.append(10)
print("adiciona o elemento 10 ao final da lista: %s" % nums)
# extend nums com os elementos de nums2
num2 = [3, 7]
nums.extend(num2)
print("extend nums com os elementos de nums2: %s" % nums)
# insere o elemento 0 na posição 2 da lista
nums.insert(2, 0)
print("insere o elemento 0 na posição 2 da lista: %s" % nums)
# remove o elemento 11 da lista
nums.remove(11)
print("remove o elemento 11 da lista: %s" % nums)
# remove e retorna o elemento na posição 7 da lista
print("remove e retorna o elemento na posição 7 da lista: %s" % nums.pop(7))
print("lista após pop(): %s" % nums)
# cria uma cópia da nums em numsCpy
numsCpy = nums.copy()
print("cria uma cópia da nums em numsCpy: %s" % nums)
# remove todos os elementos de nums
nums.clear()
print("remove todos os elementos de nums: %s" % nums)
# conta quantos elementos 8 existem na lista
nums = numsCpy.copy()
print("conta quantos elementos 8 existem na lista: %s" % nums.count(8))
# ordena nums em ordem ascendente
nums.sort()
print("ordena nums em ordem ascendente: %s" % nums)
# inverte os elementos de nums
nums.reverse()
print("inverte os elementos de nums: %s" % nums)
