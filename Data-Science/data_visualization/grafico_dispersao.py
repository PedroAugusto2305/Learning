from matplotlib import pyplot as plt

num_indications = [8, 13, 11, 5, 5]
num_oscars = [1, 7, 4, 2, 1]
movies = ["Barbie", "Oppenheimer", "Poor Things", "The Zone of Interest", "The Rejects"]

plt.scatter(num_indications, num_oscars)

for movie, indication_count, oscar_count in zip(movies, num_indications, num_oscars):
    plt.annotate(movie, xy=(indication_count, oscar_count),
                 xytext=(5, -5),
                 textcoords="offset points")
plt.title("Indicações vs Estatuetas Ganhas")
plt.xlabel("Indicações")
plt.ylabel("Estatuetas Ganhas")
plt.show()