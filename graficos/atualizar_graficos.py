import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    dados_grafico = open('atualizar_graficos.txt','r').read()
    linhas = dados_grafico.split('\n')
    xs = []
    ys = []
    for linha in linhas:
        if len(linha) > 1:
            x, y = linha.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
