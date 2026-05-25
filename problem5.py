import numpy as np


def simulate_a(n=100_000):
    # simulate scenario A: stop after first boy
    return np.random.geometric(0.5, n)


def simulate_b(n=100_000):
    # simulate scenario B: stop after both sexes
    return 1 + np.random.geometric(0.5, n)


if __name__ == "__main__":
    n = 100_000

    children_a = simulate_a(n)
    children_b = simulate_b(n)

    avg_a = np.mean(children_a)
    avg_b = np.mean(children_b)

    total_a = int(np.sum(children_a))
    total_b = int(np.sum(children_b))
    difference = total_b - total_a

    print("Scenario A (stop after first boy):")
    print(f"  Simulated average:   {avg_a:.4f}")
    print(f"  Theoretical average: 2.0000")

    print(f"\nScenario B (stop after both sexes):")
    print(f"  Simulated average:   {avg_b:.4f}")
    print(f"  Theoretical average: 3.0000")

    print(f"\nAdditional children under B for {n:,} families: {difference:,}")
