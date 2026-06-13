import random
import math


def buffon_needle_simulation(num_trials=100000):
    """
    Estimate π using Buffon's Needle experiment.

    Parameters:
        num_trials (int): Number of needle drops.

    Returns:
        float: Estimated value of π.
    """

    intersections = 0

    for _ in range(num_trials):

        # Distance from needle center to nearest line
        distance = random.uniform(0, 0.5)

        # Random angle between needle and parallel lines
        angle = random.uniform(0, math.pi / 2)

        # Check if the needle crosses a line
        if distance <= 0.5 * math.sin(angle):
            intersections += 1

    if intersections == 0:
        return None

    estimated_pi = (2 * num_trials) / intersections

    return estimated_pi


if __name__ == "__main__":

    trials = int(input("Number of simulations: "))

    estimated_pi = buffon_needle_simulation(trials)

    print(f"\nEstimated π: {estimated_pi:.6f}")
    print(f"Actual π:    {math.pi:.6f}")
    print(f"Error:       {abs(math.pi - estimated_pi):.6f}")