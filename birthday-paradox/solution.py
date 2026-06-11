import random


def has_duplicate_birthdays(group_size):
    
    # Generate random birthdays for all people in the group
    birthdays = []
    for _ in range(group_size):
        birthdays.append(random.randint(1, 365))
        
    # If duplicates exist, converting to a set will reduce the size
    return len(birthdays) != len(set(birthdays))


# Run the experiment multiple times
def estimate_probability(group_size, simulations=10000):
    duplicate_count = 0

    for _ in range(simulations):
        if has_duplicate_birthdays(group_size):
            duplicate_count += 1
            
    # Estimate probability using Monte Carlo simulation
    probability = duplicate_count / simulations

    return probability


group_size = int(input("Enter group size: "))

result = estimate_probability(group_size)

print(f"Estimated Probability: {result:.3f}")