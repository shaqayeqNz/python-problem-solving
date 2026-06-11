import random

def monty_simulation(n=10000, switch=True):
    """
    Runs a Monte Carlo simulation of the Monty Hall problem.

    This function simulates the Monty Hall game `n` times and calculates
    the probability of winning the car based on the chosen strategy.

    Parameters:
    n (int): Number of simulation runs (default is 10,000).
    switch (bool): 
        - True  → the player always switches doors.
        - False → the player always stays with the initial choice.

    Returns:
    float: The fraction of games won (estimated probability of winning).
    """
    
    wins = 0  # Counts how many times the player wins the car

    for _ in range(n):
        # Randomly place one car and two goats behind the doors
        doors = ['goat', 'car', 'goat']
        random.shuffle(doors)

        # Player randomly chooses one of the three doors (0-based index)
        first_choice = random.randint(0, 2)

        # Monty reveals one goat door that is not the player's choice
        revealed = random.choice(
            [i for i in range(3) if doors[i] == 'goat' and i != first_choice]
        )

        # Player's final decision
        if switch:
            # Switch to the only remaining unopened door
            final_choice = [i for i in range(3)
                            if i != first_choice and i != revealed][0]
        else:
            # Stay with the original door
            final_choice = first_choice

        # Check if the final choice is the car
        if doors[final_choice] == 'car':
            wins += 1

    # Return the win rate
    return wins / n

print("Switch win rate:", monty_simulation(switch=True))
print("Stay win rate:", monty_simulation(switch=False))
