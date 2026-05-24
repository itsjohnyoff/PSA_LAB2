# PSA Lab 2: Probability and Statistics Experiments

This repository contains the laboratory assignments for the Probability and Statistics (PSA) course.

## Problem 1: Galileo's Dice Paradox

### The Problem
A student observed that although the number of unordered combinations (partitions) of three dice resulting in a sum of 9 is the same as those resulting in a sum of 10, a 9 seems to come up less frequently than a 10 when three dice are rolled.

### Mathematical Insight
The student's observation is correct. This is a classic paradox famously solved by Galileo Galilei.

While both 9 and 10 have exactly 6 unique unordered combinations (partitions) using three numbers from 1 to 6, they do not have the same number of permutations (ordered outcomes) because the three dice are independent:

* **For a sum of 9:** The permutations total 25 out of 216 possible outcomes ($P(9) = \frac{25}{216} \approx 0.1157$).
* **For a sum of 10:** The permutations total 27 out of 216 possible outcomes ($P(10) = \frac{27}{216} \approx 0.1250$).

### How to Run the Simulation

The script `problem1.py` calculates the exact theoretical probabilities, runs a Monte Carlo simulation with 1,000,000 rolls, and plots a comparison.

#### Prerequisites
Install the required packages:
```bash
pip install matplotlib numpy
```

#### Running the Script
```bash
python problem1.py
```

This will display the plot and save it as `dice_paradox_results.png`.