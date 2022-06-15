# Classe (Exemplo de aplicação 1)
# Curso: Raciocínio Lógico
# Pontifícia Universidade Católica do Paraná (PUC-PR)
'''
Exemplo de aplicação 1: Elabore uma classe Quadrado, que receba em seu construtor o lado e
tenha como função para seus métodos calcular perímetro, área e diagonal, bem como um método
de impressão informando: “Quadrado de lado {lado}”. Ao final, deve testar a classe e todos
os seus métodos.
'''
from operacoes import Quadrado

if __name__ == '__main__':
    while True:
        quadrado = Quadrado(float(input("\nInsira o tamanho do lado do quadrado: ")))
        quadrado.imprimir()
        print("Perímetro:", quadrado.calc_perimetro())
        print("Área:", quadrado.calc_area())
        print(f"Diagonal: {quadrado.calc_diagonal():.2f}")
