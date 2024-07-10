from matplotlib import pyplot as plt

movies = ["Barbie", "Oppenheimer", "Poor Things", "The Zone of Interest"]
num_oscars = [1, 7, 4, 2]

plt.bar(range(len(movies)), num_oscars)

plt.title("Vencedores do Oscar 2024")
plt.ylabel("Nº de Oscars")

plt.xticks(range(len(movies)), movies)

plt.show()