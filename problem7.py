import numpy as np
import matplotlib.pyplot as plt


def simulate(n_experiments=1000, n_flips=100):
    # simulate coin tosses: each row is one experiment
    tosses = np.random.randint(0, 2, size=(n_experiments, n_flips))
    return tosses.sum(axis=1)


def plot_distribution(heads_counts):
    n_exp = len(heads_counts)

    # proportions for each value in [35, 65]
    n_values = np.arange(35, 66)
    proportions = np.array([np.sum(heads_counts == n) / n_exp for n in n_values])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(n_values, proportions, color='#2b5c8f', edgecolor='black',
           alpha=0.7, label='Simulated proportions')

    # theoretical normal curve N(50, 5^2)
    mu, sigma = 50, 5
    x = np.linspace(35, 65, 200)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    ax.plot(x, y, color='red', linewidth=2.5, label='Normal approximation')

    ax.set_xlabel('Number of Heads')
    ax.set_ylabel('Proportion')
    ax.set_title('Coin Toss Distribution vs Normal Curve')
    ax.set_xticks(range(35, 66, 5))
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig('coin_toss_normal_fit.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    heads = simulate(1000, 100)

    mean_heads = np.mean(heads)
    std_heads = np.std(heads)

    print(f"Simulated mean:   {mean_heads:.2f}")
    print(f"Theoretical mean: 50.00")
    print(f"Simulated std:    {std_heads:.2f}")
    print(f"Theoretical std:  5.00")

    plot_distribution(heads)
    print("Graph saved to coin_toss_normal_fit.png")
