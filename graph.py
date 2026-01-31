from matplotlib import pyplot as graph
from Runtime import run_experiment

n, match_times, verify_times = run_experiment()

graph.plot(n, match_times, label="Matching")
graph.plot(n, verify_times, label="Verifier")

graph.title("Gale-Shapley Running Time")
graph.ylabel("Time (s)")
graph.xlabel("N (students/hospitals)")
graph.legend()

graph.show()
