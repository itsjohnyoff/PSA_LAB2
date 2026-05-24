# PSA Lab 2: Galileo's Dice Paradox

## Overview
This repository contains the implementation for the second laboratory assignment in the Probability and Statistics (PSA) course. The project explores Galileo's Dice Paradox, which addresses the probability difference between obtaining a sum of 9 versus a sum of 10 when rolling three fair six-sided dice.

## Problem Description
A classic question in probability asks why a sum of 10 appears more frequently than a sum of 9 when rolling three dice, even though both sums can be formed by the same number of unordered combinations (partitions). 

Unordered partitions:
* **Sum of 9:** (1,2,6), (1,3,5), (1,4,4), (2,2,5), (2,3,4), (3,3,3) — 6 partitions
* **Sum of 10:** (1,3,6), (1,4,5), (2,2,6), (2,3,5), (2,4,4), (3,3,4) — 6 partitions

Despite having the same number of partitions, experimental trials show that a sum of 10 occurs more often than a sum of 9.

## Mathematical Explanation
The paradox is resolved by considering the ordered outcomes (permutations). Since the three dice are independent and distinguishable, each partition has a different number of permutations based on its elements:

* Distinct numbers (e.g., 1, 2, 6) have 3! = 6 permutations.
* Partitions with two repeating numbers (e.g., 1, 4, 4) have 3! / 2! = 3 permutations.
* Partitions with three repeating numbers (e.g., 3, 3, 3) have 3! / 3! = 1 permutation.

### Permutations for Sum 9:
* (1,2,6) -> 6 permutations
* (1,3,5) -> 6 permutations
* (1,4,4) -> 3 permutations
* (2,2,5) -> 3 permutations
* (2,3,4) -> 6 permutations
* (3,3,3) -> 1 permutation
* **Total Permutations:** 6 + 6 + 3 + 3 + 6 + 1 = 25
* **Theoretical Probability:** P(9) = 25 / 216 ≈ 0.1157

### Permutations for Sum 10:
* (1,3,6) -> 6 permutations
* (1,4,5) -> 6 permutations
* (2,2,6) -> 3 permutations
* (2,3,5) -> 6 permutations
* (2,4,4) -> 3 permutations
* (3,3,4) -> 3 permutations
* **Total Permutations:** 6 + 6 + 3 + 6 + 3 + 3 = 27
* **Theoretical Probability:** P(10) = 27 / 216 = 0.1250

## Methodology
The solution is implemented in `problem1.py` and consists of two main parts:
1. **Theoretical Computation:** A brute-force calculation over all 216 possible outcomes to count the exact permutations for each sum (from 3 to 18) and calculate their exact probabilities.
2. **Monte Carlo Simulation:** A simulation of 1,000,000 trials of rolling three independent dice, computing the empirical frequencies of each sum.
3. **Data Visualization:** Plotting the comparison between the theoretical and experimental results and saving it as an image.

## Project Structure
```text
.
├── problem1.py                 # Main Python script containing the math, simulation, and plotting
├── dice_paradox_results.png    # Generated chart comparing theoretical and experimental probabilities
└── README.md                   # Project documentation
```

## Technologies Used
* **Python 3**
* **NumPy** - for numerical data structuring
* **Matplotlib** - for generating the probability distribution chart

## Installation & Setup
To run this project locally, ensure you have Python 3 installed. Install the required dependencies using pip:

```bash
pip install numpy matplotlib
```

## Usage
Run the script using the command:

```bash
python problem1.py
```

## Example Output
Running the script outputs the following console text:

```text
Combinations resulting in 9: 25 (P = 0.1157)
Combinations resulting in 10: 27 (P = 0.1250)
Graph saved to dice_paradox_results.png
```

## Results
The comparison confirms the theoretical analysis. The empirical probabilities closely match the theoretical outcomes, showing the distinct difference between 9 and 10. The output visualization is saved in the repository as `dice_paradox_results.png`.