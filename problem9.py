import numpy as np


def simulate(n_games):
    # sample threshold X
    x = np.random.uniform(0, 1, n_games)

    # simulate geometric stopping times and compute payouts
    payouts = np.random.geometric(1 - x) - 1
    return np.mean(payouts)


if __name__ == "__main__":
    print("Random Variables Game Simulation\n")

    test_sizes = [1_000, 10_000, 100_000, 1_000_000]
    for size in test_sizes:
        avg_payout = simulate(size)
        print(f"Games: {size:9,} | Average payout: ${avg_payout:.4f}")

    print("\nConclusion:")
    print("  The theoretical expected payout is infinite (integral of x / (1-x) from 0 to 1).")
    print("  As the number of games increases, the empirical average grows because the probability")
    print("  of sampling an X close to 1 increases, resulting in very large payouts.")