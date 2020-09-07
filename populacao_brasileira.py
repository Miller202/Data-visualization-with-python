import matplotlib.pyplot as plt

data = open("populacao_brasileira.csv").readlines()

x = [] #Anos
y = [] #População

for i in range(len(data)):
	if i != 0:
		lign = data[i].split(";")
		x.append(int(lign[0]))
		y.append(int(lign[1]))

plt.plot(x, y, color="k")
plt.bar(x, y, color="#a9a9a9")
plt.title("Crescimento da população brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x 100.000.000")
#plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)