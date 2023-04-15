import matplotlib
from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(
    x_values,
    y_values,
    s=30,
    c=y_values,
    cmap=plt.cm.copper,
)

ax.set_title("Cubes")
ax.set_xlabel("Values")
ax.set_xlabel("Cube values")

ax.tick_params(axis="both", which="major", labelsize=14)

ax.axis((0, 6, 0, 130))

plt.savefig("cubes_plot.png")
plt.show()
