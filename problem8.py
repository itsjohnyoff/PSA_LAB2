import numpy as np
import math


def simulate(n_participants, n_trials=100_000):
    # generate random dinner seatings
    dinner = np.array([np.random.permutation(n_participants) for _ in range(n_trials)])

    # compute adjacent differences wrapping around
    diffs = np.abs(dinner - np.roll(dinner, -1, axis=1))

    # check for common adjacent pairs
    has_common = np.any((diffs == 1) | (diffs == n_participants - 1), axis=1)

    # estimate probability
    return np.mean(~has_common)


if __name__ == "__main__":
    n_trials = 100_000

    print("Conference Seating Problem Simulation (Lunch vs Dinner)\n")

    # primary scenario for n = 10
    prob_10 = simulate(10, n_trials)
    print(f"For n = 10:")
    print(f"  Simulated probability:   {prob_10:.4f}")
    print(f"  Theoretical asymptotic:  {math.exp(-2):.4f} (e^-2)")

    print("\nInvestigating behavior as n increases:")
    print(f"{'n':<6} | {'Simulated Prob':<16} | {'Asymptotic (e^-2)':<18}")
    print("-" * 46)
    for n in [5, 10, 15, 20, 30, 50, 100]:
        prob_n = simulate(n, n_trials)
        print(f"{n:<6} | {prob_n:<16.4f} | {math.exp(-2):<18.4f}")

    print("\nConjecture for large n:")
    print("  As n -> infinity, the expected number of common adjacent pairs converges to 2.")
    print("  By Poisson approximation, the probability of zero common pairs converges to e^-2 ~ 0.1353.")
