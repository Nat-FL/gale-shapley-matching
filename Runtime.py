import time
import matplotlib.pyplot as plt
from ProgrammingAssignment1 import run_matching
import validity_check
import random


#generate random text files of size n
def generate_input(n, filename="exampleData.txt"):
    with open(filename, "w") as f:
        f.write(f"{n}\n")
        for i in range(n):  
            prefs = []
            for j in range(1,n+1):
                prefs.append(j)
            random.shuffle(prefs)
            f.write(f"{' '.join(map(str, prefs))}\n")
        for i in range(n):  
            prefs = []
            for j in range(1,n+1):
                prefs.append(j)
            random.shuffle(prefs)
            f.write(f"{' '.join(map(str, prefs))}\n")



sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

match_times = []
verify_times = []


def run_experiment():
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    match_times = []
    verify_times = []

    for n in sizes:
        generate_input(n)

        start = time.perf_counter()
        pairs, hospitals, students, n_val = run_matching(verbose=False)
        end = time.perf_counter()
        match_times.append(end - start)

        start = time.perf_counter()
        validity_check.check_stability(n_val, pairs, hospitals, students)
        end = time.perf_counter()
        verify_times.append(end - start)

    return sizes, match_times, verify_times


if __name__ == "__main__":
    run_experiment()
