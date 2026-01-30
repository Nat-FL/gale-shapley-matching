from matplotlib import pyplot as graph

n = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512] #students/hospitals
time = [.0009, .00086, .0009, 8, 16, 32, 64, 128, 256, 512] #program running time

graph.plot(n, time)
graph.title("Gale-Shapley Running Time")
graph.ylabel("Time (s)")
graph.xlabel("N (students/hospitals)")
graph.show()