# Birthday Paradox

## Description

This project estimates the probability that at least two people in a group share the same birthday.

Instead of using the mathematical formula, the solution relies on a Monte Carlo simulation by generating random birthdays and repeating the experiment thousands of times.

---

## Problem

Given a group of `n` people:

1. Assign a random birthday (1–365) to each person.
2. Check whether at least two people share the same birthday.
3. Repeat the experiment many times.
4. Estimate the probability of a shared birthday.

---

## Example

Input:

23

Output (approximate):

Estimated Probability: 0.507

The exact value may vary because birthdays are generated randomly.

---

## How It Works

The program generates a random birthday for every person in the group.

To detect duplicates efficiently, it compares:

* The length of the original list
* The length of the corresponding set

Since sets only store unique values, a difference in size indicates that at least one birthday appears more than once.

---

## Complexity

For a group of size `n`:

* Time Complexity: O(n)
* Space Complexity: O(n)

---

## Run

```bash
python solution.py
```

Example:

```text
Enter group size: 23
Estimated Probability: 0.507
```
