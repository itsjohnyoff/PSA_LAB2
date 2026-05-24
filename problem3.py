import numpy as np
import math


def simulate(n=1_000_000):
    # break stick at a random point
    first_cut = np.random.uniform(0, 1, n)
    shorter = np.minimum(first_cut, 1 - first_cut)
    longer = np.maximum(first_cut, 1 - first_cut)

    # break the longer piece at a random point
    second_cut = np.random.uniform(0, 1, n) * longer

    # three resulting pieces
    p1 = shorter
    p2 = second_cut
    p3 = longer - second_cut

    # triangle condition: largest piece must be less than 0.5
    max_piece = np.maximum(p1, np.maximum(p2, p3))
    return np.mean(max_piece < 0.5)


if __name__ == "__main__":
    exp_prob = simulate(1_000_000)
    theo_prob = 2 * math.log(2) - 1

    print(f"Simulated probability:   {exp_prob:.4f}")
    print(f"Theoretical probability: {theo_prob:.4f}")
