import matplotlib.pyplot as plt

points = []

file = open("data.csv", "r")
file.readline()
for i in file:
	i = i.replace("\n", "")
	x = i.split(",")
	points.append(x)
	plt.plot(x[1], x[0], "ro")

print(points)

plt.show()