from matplotlib import pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
pib = [7.39, 7.61, 9.01, 10.08, 10.9]

plt.plot(years, pib, color="green", marker="o", linestyle="solid")

plt.title("PIB 5 anos")

plt.xlabel("Anos")
plt.ylabel("Trilhões de Reais")

plt.xticks(years) # define os rótulos do eixo x para serem apenas valores inteiros
plt.show()