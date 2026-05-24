# PSA Laboratory Assignments

## Overview

This repository contains two laboratory assignments for the Probability and Statistics (PSA) course. Each assignment combines mathematical analysis with simulation to verify probabilistic results empirically.

---

## Problem 1 — Galileo's Dice Paradox

### Problem Statement

When rolling three fair six-sided dice, both a sum of 9 and a sum of 10 can be formed from exactly 6 unordered combinations (partitions). Despite this, empirical observation shows that a sum of 10 occurs more frequently than a sum of 9.

### Mathematical Explanation

The paradox is resolved by counting ordered outcomes (permutations), not partitions. Since the three dice are independent, each combination has a different number of permutations depending on how many elements repeat.

**Sum of 9 — ordered outcomes:**

| Partition  | Permutations |
|------------|-------------|
| (1, 2, 6)  | 6           |
| (1, 3, 5)  | 6           |
| (1, 4, 4)  | 3           |
| (2, 2, 5)  | 3           |
| (2, 3, 4)  | 6           |
| (3, 3, 3)  | 1           |
| **Total**  | **25**      |

P(9) = 25 / 216 ≈ 0.1157

**Sum of 10 — ordered outcomes:**

| Partition  | Permutations |
|------------|-------------|
| (1, 3, 6)  | 6           |
| (1, 4, 5)  | 6           |
| (2, 2, 6)  | 3           |
| (2, 3, 5)  | 6           |
| (2, 4, 4)  | 3           |
| (3, 3, 4)  | 3           |
| **Total**  | **27**      |

P(10) = 27 / 216 ≈ 0.1250

### Methodology

1. **Theoretical computation** — brute-force enumeration of all 6³ = 216 outcomes.
2. **Monte Carlo simulation** — 1,000,000 rolls of three independent dice using NumPy.
3. **Visualization** — side-by-side bar chart comparing theoretical and experimental probabilities.

### Results

```
Combinations resulting in 9:  25  (P = 0.1157)
Combinations resulting in 10: 27  (P = 0.1250)
Graph saved to dice_paradox_results.png
```

The simulation closely matches the theoretical values, confirming that sum 10 is more probable than sum 9.

### Generated Graph

![Distribution of Sums for Three Dice](dice_paradox_results.png)

---

## Problem 2 — National Election Simulation

### Problem Statement

A pollster samples a subset of voters to predict the winner of a two-candidate election. The goal is to determine how often the pollster correctly identifies the winner across 100 repeated trials, under different sample sizes and probability splits.

### Simulation Approach

Each trial draws a random sample of voters. Each voter independently votes Democrat with probability `p` and Republican with probability `1 - p`. The pollster predicts Democrat wins if more than half the sampled votes are Democrat. This is repeated 100 times per scenario.

### Scenarios Tested

| Sample Size | Democrat % | Republican % |
|-------------|-----------|-------------|
| 1000        | 52%       | 48%         |
| 1000        | 51%       | 49%         |
| 3000        | 52%       | 48%         |
| 3000        | 51%       | 49%         |

### Interpretation of Results

A larger sample size reduces variance and leads to more consistent correct predictions. A smaller margin between candidates (51/49) makes the pollster's task harder, so correct predictions drop compared to the 52/48 split. Increasing the sample size from 1000 to 3000 compensates for the smaller margin.

---

## Installation

Requires Python 3. Install dependencies:

```bash
pip install numpy matplotlib
```

---

## Usage

Run each problem independently:

```bash
python problem1.py
python problem2.py
```

---

## Repository Structure

```text
.
├── problem1.py                # Galileo's Dice Paradox — theory, simulation, and plot
├── problem2.py                # Election polling simulation
├── dice_paradox_results.png   # Output graph from problem1.py
└── README.md
```

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib