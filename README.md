# PSA Laboratory Assignments

## Overview

This repository contains two laboratory assignments for the Probability and Statistics (PSA) course. Both problems use Python to combine analytical computation with Monte Carlo simulation, allowing theoretical probability results to be verified empirically.

---

## Problem 1 – Galileo's Dice Paradox

### Problem Statement

When rolling three fair six-sided dice, both a sum of 9 and a sum of 10 can be formed from exactly six unordered combinations (partitions). Despite this symmetry, empirical observation shows that a sum of 10 occurs more frequently than a sum of 9. The goal of this problem is to explain and verify this result mathematically and through simulation.

### Mathematical Background

The paradox is resolved by counting ordered outcomes (permutations) rather than unordered partitions. Since the three dice are distinguishable and independent, combinations with repeated values produce fewer arrangements than those with all distinct values.

The total number of possible outcomes when rolling three dice is 6³ = 216.

**Sum of 9 – ordered outcomes:**

| Partition | Permutations |
|-----------|-------------|
| (1, 2, 6) | 6 |
| (1, 3, 5) | 6 |
| (1, 4, 4) | 3 |
| (2, 2, 5) | 3 |
| (2, 3, 4) | 6 |
| (3, 3, 3) | 1 |
| **Total** | **25** |

P(sum = 9) = 25 / 216 ≈ 0.1157

**Sum of 10 – ordered outcomes:**

| Partition | Permutations |
|-----------|-------------|
| (1, 3, 6) | 6 |
| (1, 4, 5) | 6 |
| (2, 2, 6) | 3 |
| (2, 3, 5) | 6 |
| (2, 4, 4) | 3 |
| (3, 3, 4) | 3 |
| **Total** | **27** |

P(sum = 10) = 27 / 216 ≈ 0.1250

Sum 10 has two more ordered outcomes than sum 9, making it strictly more probable despite both having the same number of partitions.

### Methodology

1. **Exhaustive enumeration** – All 216 ordered outcomes are counted by iterating over every possible combination of three dice values. Exact probabilities are computed directly from the counts.
2. **Monte Carlo simulation** – Three dice are rolled 1,000,000 times using NumPy's random number generator. The empirical frequency of each sum is recorded.
3. **Probability comparison** – Theoretical and experimental probabilities are compared side by side for all sums from 3 to 18.
4. **Graph generation** – Results are displayed as a grouped bar chart and saved to `dice_paradox_results.png`.

### Output

Running `problem1.py` prints the following to the console:

```
Combinations resulting in 9:  25  (P = 0.1157)
Combinations resulting in 10: 27  (P = 0.1250)
Graph saved to dice_paradox_results.png
```

A bar chart comparing theoretical and experimental probabilities for all possible sums is generated and saved as `dice_paradox_results.png`. Sums 9 and 10 are highlighted on the x-axis for clarity.

![](dice_paradox_results.png)

---

## Problem 2 – National Election Simulation

### Problem Statement

A pollster conducts a random sample of voters prior to an election between two candidates (Democrat and Republican) to predict the winner. The simulation models how often the pollster's prediction is correct across 100 repeated trials, under varying sample sizes and vote distributions.

### Simulation Method

Each trial proceeds as follows:

1. A random sample of `n` voters is drawn from the population.
2. Each voter independently votes Democrat with probability `p` and Republican with probability `1 − p`.
3. The pollster predicts a Democrat win if more than half of the sampled votes are Democrat.
4. The prediction is compared against the known true majority.

This process is repeated 100 times per scenario. The output reports how many of the 100 trials resulted in a correct prediction.

### Scenarios Tested

| Sample Size | Democrat | Republican |
| ----------- | -------- | ---------- |
| 1000        | 52%      | 48%        |
| 1000        | 51%      | 49%        |
| 3000        | 52%      | 48%        |
| 3000        | 51%      | 49%        |

### Interpretation

- **Sample size effect** – Larger samples reduce sampling variability. With 3000 voters, the poll results are more consistent and the correct winner is identified more reliably than with 1000 voters.
- **Margin effect** – A 51/49 split is harder to predict correctly than a 52/48 split. The smaller the true margin, the greater the chance that random sampling fluctuations lead the poll to favour the wrong candidate.
- **Combined effect** – Increasing the sample size partially compensates for a narrow margin. The 3000-voter / 51% Democrat scenario performs noticeably better than the 1000-voter equivalent.

Since both programs use random sampling, results will vary slightly between executions. This variability is itself a demonstration of sampling uncertainty.

---

## Installation

Requires Python 3. Install dependencies with:

```bash
pip install numpy matplotlib
```

---

## Usage

Run each script independently from the project directory:

```bash
python problem1.py
python problem2.py
```

---

## Repository Structure

```
.
├── problem1.py                # Galileo's Dice Paradox – enumeration, simulation, and plot
├── problem2.py                # Election polling simulation
├── dice_paradox_results.png   # Bar chart generated by problem1.py
└── README.md
```

---

## Technologies Used

* Python 3
* NumPy
* Matplotlib

---

## Key Concepts

- Probability theory and combinatorics
- Monte Carlo simulation
- Random sampling and polling models
- Statistical inference under uncertainty