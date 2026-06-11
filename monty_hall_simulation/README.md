# Monty Hall Simulation

## Description

This project uses a Monte Carlo simulation to explore the famous Monty Hall problem.

The simulation compares two strategies:

* Always stay with the initial choice
* Always switch after the host reveals a goat

The goal is to estimate the probability of winning the car under each strategy.

---

## The Monty Hall Problem

A contestant is presented with three doors:

* One door hides a car.
* Two doors hide goats.

The contestant chooses one door.

The host, who knows where the car is, opens one of the remaining doors and reveals a goat.

The contestant then has two options:

1. Stay with the original choice.
2. Switch to the other unopened door.

Which strategy gives a higher chance of winning?

---

## Simulation Approach

The program simulates the game thousands of times.

For each game:

1. Randomly place the car.
2. Let the player choose a door.
3. Reveal a goat door.
4. Apply the selected strategy.
5. Record whether the player wins.

The final win rate is calculated as:

Win Rate = Wins / Number of Simulations

---

## Concepts Used

* Python Functions
* Random Module
* Monte Carlo Simulation
* Probability
* Conditional Decision Making

---

## Expected Results

After a large number of simulations:

| Strategy | Approximate Win Rate |
| -------- | -------------------- |
| Stay     | ~33%                 |
| Switch   | ~66%                 |

The exact values vary slightly due to randomness.

---

## Run

```bash
python solution.py
```

Example Output:

```text
Switch win rate: 0.6674
Stay win rate: 0.3331
```

---

## Complexity

For `n` simulations:

* Time Complexity: O(n)
* Space Complexity: O(1)

---

## Key Insight

Switching doors approximately doubles the probability of winning.

The simulation confirms the mathematical result that:

* Staying wins about 1/3 of the time.
* Switching wins about 2/3 of the time.
