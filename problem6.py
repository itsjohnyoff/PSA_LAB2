import numpy as np


def simulate(n=1_000_000):
    # coin radius r, square side = 4r
    # coin fits inside if center is in [r, 3r] x [r, 3r]
    # probability = (2r)^2 / (4r)^2 = 1/4
    side = 4.0
    r = 1.0

    x = np.random.uniform(0, side, n)
    y = np.random.uniform(0, side, n)

    # check if coin center is far enough from all edges
    inside = (x > r) & (x < side - r) & (y > r) & (y < side - r)
    return np.mean(inside)


if __name__ == "__main__":
    n = 1_000_000
    exp_prob = simulate(n)
    theo_prob = 0.25

    cost = 0.25
    payout = 1.00
    ev = theo_prob * payout - cost

    print(f"Simulated probability:   {exp_prob:.4f}")
    print(f"Theoretical probability: {theo_prob:.4f}")
    print(f"Expected value per toss: {ev:.4f} lei")
    print(f"Conclusion: the game is fair (EV = 0)")
