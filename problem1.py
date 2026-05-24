import random
import matplotlib.pyplot as plt
import numpy as np


def calculate_theoretical_probabilities():
    # just brute-force all 6*6*6 = 216 possible rolls and count each sum
    counts = {s: 0 for s in range(3, 19)}
    total = 6 ** 3

    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                counts[d1 + d2 + d3] += 1

    # turn raw counts into probabilities
    probs = {s: c / total for s, c in counts.items()}
    return probs, counts


def simulate_dice_rolls(n=1_000_000):
    # roll 3 dice a million times and track how often each sum appears
    counts = {s: 0 for s in range(3, 19)}

    for _ in range(n):
        roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        counts[roll] += 1

    # convert to relative frequencies so we can compare with theory
    probs = {s: c / n for s, c in counts.items()}
    return probs


def plot_results(theoretical, experimental):
    sums = list(theoretical.keys())
    theo_vals = list(theoretical.values())
    exp_vals = list(experimental.values())

    x = np.arange(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    # side-by-side bars: blue for theory, orange for experiment
    ax.bar(x - width / 2, theo_vals, width, label='Theoretical', color='#2b5c8f')
    ax.bar(x + width / 2, exp_vals, width, label='Experimental (1M rolls)', color='#d95f02', alpha=0.85)

    ax.set_xlabel('Sum of Three Dice', fontsize=12)
    ax.set_ylabel('Probability', fontsize=12)
    ax.set_title("Galileo's Dice Paradox: Sum of 9 vs. Sum of 10", fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend(fontsize=11)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # make the 9 and 10 labels stand out on the x-axis
    ax.get_xticklabels()[9 - 3].set_color('red')
    ax.get_xticklabels()[9 - 3].set_fontweight('bold')
    ax.get_xticklabels()[10 - 3].set_color('green')
    ax.get_xticklabels()[10 - 3].set_fontweight('bold')

    # little info box in the corner with the exact numbers for 9 and 10
    info = (f"Sum 9 Theo:  {theoretical[9]:.4f}\n"
            f"Sum 9 Exp:   {experimental[9]:.4f}\n\n"
            f"Sum 10 Theo: {theoretical[10]:.4f}\n"
            f"Sum 10 Exp:  {experimental[10]:.4f}")

    box_style = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, info, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=box_style, fontfamily='monospace')

    plt.tight_layout()
    plt.savefig('dice_paradox_results.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    # --- step 1: exact math ---
    print("Calculating theoretical values...")
    theo_probs, theo_counts = calculate_theoretical_probabilities()

    # 25 vs 27 ordered outcomes — that's the whole paradox
    print(f"Combinations resulting in 9:  {theo_counts[9]}  (P = {theo_probs[9]:.4f})")
    print(f"Combinations resulting in 10: {theo_counts[10]}  (P = {theo_probs[10]:.4f})")

    # --- step 2: back it up with a simulation ---
    print("\nRunning Monte Carlo simulation (1 000 000 rolls)...")
    exp_probs = simulate_dice_rolls(1_000_000)

    # --- step 3: visualise ---
    print("\nPlotting results...")
    plot_results(theo_probs, exp_probs)
    print("Done — saved as 'dice_paradox_results.png'.")
