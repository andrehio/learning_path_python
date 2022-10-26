import os
import stat
import time

# Apenas permissao de leitura para o proprietário
# os.chmod("exemplo.txt", stat.S_IRUSR)

# Dar permissão de leitura, escrita e execução ao proprietário
# os.chmod("exemplo.txt", stat.S_IRWXU)

nova_linha = ""

if os.path.isfile("permissao.txt"):
    os.chmod("permissao.txt", stat.S_IRWXU)
    arquivo = open("permissao.txt", "a")
    nova_linha = "\n"
else:
    arquivo = open("permissao.txt", "w")


segundos = time.time()
data = time.ctime(segundos)
arquivo.write(nova_linha + data)
arquivo.close()

os.chmod("permissao.txt", stat.S_IRUSR)
