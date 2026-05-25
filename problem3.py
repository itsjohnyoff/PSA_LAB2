import numpy as np
import math


def simulate(n=1_000_000):
    # simulate first break of the stick
    first_cut = np.random.uniform(0, 1, n)
    shorter = np.minimum(first_cut, 1 - first_cut)
    longer = np.maximum(first_cut, 1 - first_cut)

    # simulate second break on the longer piece
    second_cut = np.random.uniform(0, 1, n) * longer

    # define lengths of the three pieces
    p1 = shorter
    p2 = second_cut
    p3 = longer - second_cut

    # check if the pieces can form a triangle
    max_piece = np.maximum(p1, np.maximum(p2, p3))
    return np.mean(max_piece < 0.5)


if __name__ == "__main__":
    exp_prob = simulate(1_000_000)
    theo_prob = 2 * math.log(2) - 1

    print(f"Simulated probability:   {exp_prob:.4f}")
    print(f"Theoretical probability: {theo_prob:.4f}")
