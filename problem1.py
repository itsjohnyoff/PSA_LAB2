import numpy as np
import matplotlib.pyplot as plt


def get_theoretical():
    # count all possible outcomes for sums of 3 dice
    counts = {s: 0 for s in range(3, 19)}
    total = 6 ** 3
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                counts[d1 + d2 + d3] += 1
    probs = {s: c / total for s, c in counts.items()}
    return probs, counts


def simulate(n=1_000_000):
    # Monte Carlo simulation using numpy for speed
    rolls = np.random.randint(1, 7, size=(n, 3)).sum(axis=1)
    counts = {s: int(np.sum(rolls == s)) for s in range(3, 19)}
    probs = {s: c / n for s, c in counts.items()}
    return probs


def plot_results(theo, exp):
    # compare theoretical and experimental distributions
    sums = list(theo.keys())
    x = np.arange(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width / 2, list(theo.values()), width, label='Theoretical', color='#2b5c8f')
    ax.bar(x + width / 2, list(exp.values()), width, label='Experimental', color='#d95f02', alpha=0.85)

    ax.set_xlabel('Sum of Three Dice')
    ax.set_ylabel('Probability')
    ax.set_title('Distribution of Sums for Three Dice')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # highlight sums 9 and 10
    ax.get_xticklabels()[9 - 3].set_color('red')
    ax.get_xticklabels()[9 - 3].set_fontweight('bold')
    ax.get_xticklabels()[10 - 3].set_color('green')
    ax.get_xticklabels()[10 - 3].set_fontweight('bold')

    info = (f"Sum 9 Theo:  {theo[9]:.4f}\n"
            f"Sum 9 Exp:   {exp[9]:.4f}\n\n"
            f"Sum 10 Theo: {theo[10]:.4f}\n"
            f"Sum 10 Exp:  {exp[10]:.4f}")
    box_style = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, info, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=box_style, fontfamily='monospace')

    plt.tight_layout()
    # save figure
    plt.savefig('dice_paradox_results.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    theo_probs, theo_counts = get_theoretical()
    exp_probs = simulate(1_000_000)

    print(f"Combinations resulting in 9:  {theo_counts[9]}  (P = {theo_probs[9]:.4f})")
    print(f"Combinations resulting in 10: {theo_counts[10]}  (P = {theo_probs[10]:.4f})")

    plot_results(theo_probs, exp_probs)
    print("Graph saved to dice_paradox_results.png")
