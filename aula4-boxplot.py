import matplotlib.pyplot as plt
import random

array = []

for i in range(10):
	number = random.randint(0,5)
	array.append(number)

plt.boxplot(array)
plt.title("Meu Boxplot")
plt.show()
