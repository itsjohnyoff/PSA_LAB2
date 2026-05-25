import numpy as np


def simulate(n=1_000_000):
    # sample and sort four random points on a circle
    points = np.sort(np.random.uniform(0, 1, (n, 4)), axis=1)

    # compute consecutive arc lengths
    a = points[:, 1] - points[:, 0]
    b = points[:, 2] - points[:, 1]
    c = points[:, 3] - points[:, 2]

    # check angle constraints for the quadrilateral
    u = a + b
    v = b + c
    mask = (u > 1/3) & (u < 2/3) & (v > 1/3) & (v < 2/3)

    return np.mean(mask)


if __name__ == "__main__":
    exp_prob = simulate(1_000_000)
    theo_prob = 7 / 27

    print(f"Simulated probability:   {exp_prob:.4f}")
    print(f"Theoretical probability: {theo_prob:.4f}")
