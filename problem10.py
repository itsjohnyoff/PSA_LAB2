import numpy as np


def simulate(n_simulations=100_000, n_rides=730):
    # sample ticket purchases (muscular collector)
    tickets = np.random.binomial(n_rides, 0.02, n_simulations)

    # sample offenses from remaining rides (caught by controller)
    offenses = np.random.binomial(n_rides - tickets, 0.05)

    # calculate fine costs based on offense counts
    fine_costs = np.zeros(n_simulations)
    fine_costs[offenses == 1] = 50
    fine_costs[offenses == 2] = 250
    fine_costs[offenses >= 3] = 300 * offenses[offenses >= 3] - 350

    # calculate total annual cost
    return tickets * 7 + fine_costs


if __name__ == "__main__":
    n_simulations = 100_000
    n_rides = 730

    print(f"Simulating {n_simulations:,} years of trolleybus rides...\n")

    costs = simulate(n_simulations, n_rides)
    avg_jora_cost = np.mean(costs)
    student_cost = n_rides * 7

    print("--- Results ---")
    print(f"Expected annual cost for Jora:      {avg_jora_cost:.2f} lei")
    print(f"Annual cost for law-abiding student: {student_cost:.2f} lei")

    print("\n--- Conclusion ---")
    if avg_jora_cost > student_cost:
        print(f"Fare evasion is not advantageous. Jora pays {avg_jora_cost - student_cost:.2f} lei more on average.")
    else:
        print("Fare evasion is advantageous on average.")
