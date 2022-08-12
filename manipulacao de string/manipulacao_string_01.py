# Manipulação de string 01

# String em analise
texto = "Eu moro no Brasil"
print("texto:", texto)

# Fatiamento
print("\n----Fatiamento----")
print("texto[9]:", texto[9])
print("texto[9:13]:",texto[9:13]) # o ultimo (13) não entra na contagem.
print("texto[9:17]:",texto[9:17])
print("texto[9:17:2]:",texto[9:17:2]) # com passo de 2 em 2
print("texto[:5]:",texto[:5]) # começa do zero
print("texto[6:]:",texto[6:]) # começa no 6 e termina até o final da string
print("texto[6::3]:",texto[6::3])

# Análise
print("\n----Análise----")
print("len (tamanho da string):", len(texto))
print("count:", texto.count("o")) # conta quantas vezes aparece a letra "o".
print("count:", texto.count("o", 0, 7)) # count com analise limitada
print("find:", texto.find("oro")) # indica a posição que começou o "oro"
print("find:", texto.find("Espanha")) # se nao for encontrado, retorna -1
print("Brasil" in texto) # true ou false se a string analisada existe

# Transformação
print("\n----Transformação----")
print("replace:", texto.replace("Brasil", "Peru"))
print("upper:", texto.upper())
print("lower:", texto.lower())
print("capitalize:", texto.capitalize())
print("title:", texto.title())

texto_com_espaços_iniciais = "   Aprenda Python  "
print("texto_com_espaços_iniciais:", texto_com_espaços_iniciais)
print("strip:", texto_com_espaços_iniciais.strip()) # remove todos os espaços no inicio e final
# da string.
print("rstrip:", texto_com_espaços_iniciais.rstrip()) # remove espaços right
print("lstrip:", texto_com_espaços_iniciais.lstrip()) # remove espaços left

# Divisão
print("\n----Divisão----")
print("split:", texto.split()) # Divide a string em varias dentro de uma lista
print("join:", "-".join(texto.split()))