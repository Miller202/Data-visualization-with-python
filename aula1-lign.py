import matplotlib.pyplot as plt

x = [1, 2]
y = [2, 5]

titulo = "Gráfico padrão"
eixoX = "Eixo X"
eixoY = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.plot(x, y)
plt.show()