import matplotlib.pyplot as plt

from randomwalk import RandomWalk


rw = RandomWalk(50000)
rw.fill_walk()

plt.figure(figsize=(10,6), dpi=120)

point_numbers = list(range(rw.num_points))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=2)

plt.axis("off")


plt.show()

    

    