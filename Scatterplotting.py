import matplotlib.pyplot as plt

day = [10, 20, 30, 40, 50, 60]  #day is variable and value are parameters
month = [1, 2, 3, 4, 5, 6]
color = [10, 20, 30, 40, 50, 60]
sizes = [100, 200, 300, 400, 500, 600]

plt.scatter(day, month, s=sizes,alpha=0.5, c=color,marker="*",cmap="magma")
plt.grid()
plt.colorbar()

plt.title("scatter", color="r", fontsize=30)
plt.xlabel("day", color="g", fontsize=10)
plt.ylabel("month", color="y", fontsize=20)



