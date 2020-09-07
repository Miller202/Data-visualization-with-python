import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [210, 150, 400, 3000, 270]

titulo = "Scatterplot: Gráfico de dispersão"
eixoX = "Eixo X"
eixoY = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.legend()

#plt.show()
plt.savefig("figura1.png", dpi=300)