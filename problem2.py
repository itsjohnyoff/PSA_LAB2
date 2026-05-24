import numpy as np


def run_poll(sample_size, dem_prob):
    # sample individual votes and check if Democrat wins the poll
    votes = np.random.random(sample_size)
    dem_votes = np.sum(votes < dem_prob)
    return dem_votes > sample_size / 2


def run_experiment(sample_size, dem_prob, num_trials=100):
    # run 100 polling trials and count correct predictions
    correct = sum(run_poll(sample_size, dem_prob) for _ in range(num_trials))
    return correct


if __name__ == "__main__":
    # 4 scenarios: two sample sizes x two probability splits
    scenarios = [
        (1000, 0.52),
        (1000, 0.51),
        (3000, 0.52),
        (3000, 0.51),
    ]

    print("US Election Polling Simulation (100 trials per scenario)\n")

    for sample_size, dem_prob in scenarios:
        correct = run_experiment(sample_size, dem_prob)
        dem_pct = int(dem_prob * 100)
        rep_pct = 100 - dem_pct
        print(f"Sample: {sample_size} | Reality: {rep_pct}% Rep / {dem_pct}% Dem")
        print(f"Correct predictions: {correct} / 100\n")
