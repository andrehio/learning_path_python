# Classe (Exemplo de aplicação 2)
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Exemplo de aplicação 2: Elabore uma classe que simule um dado de jogo. No construtor, 
deve-se informar quantas faces possui o dado. Caso o valor informado seja inválido, 
o dado será padrão, de seis faces. Deve ter um método privado de calcular a jogada e 
um método público de retorno do valor do dado para o usuário. Ao final, deve testar  
a classe e todos os seus métodos.
'''
from dado import Dado
        
if __name__ == '__main__':
    while True:
        dado = Dado(int(input("\nInsira a quantidade de faces do dado: ")))
        print(dado.valor_jogada())
