# Buffon's Needle Simulation

## Overview

Buffon's Needle is a famous probability experiment proposed by Georges-Louis Leclerc, Comte de Buffon, in the 18th century.

The experiment estimates the value of π using random sampling and geometric probability.

This project uses a Monte Carlo simulation to reproduce Buffon's Needle experiment and approximate π.

---

## The Problem

Imagine a floor marked with equally spaced parallel lines.

A needle of length equal to the distance between the lines is dropped randomly onto the floor.

The question is:

**What is the probability that the needle crosses one of the lines?**

The surprising result is that the answer is directly related to π.

---

## Mathematical Background

For a needle whose length equals the spacing between lines:

P(crossing) = 2 / π

Rearranging gives:

π ≈ 2N / H

Where:

* N = total number of needle drops
* H = number of crossings

---

## Example

Input:

```text
100000
```

Output:

```text
Estimated π: 3.142816
Actual π:    3.141593
Error:       0.001223
```

Results vary slightly due to randomness.

---

## Complexity

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1)
```

where n is the number of needle drops.

---

## Run

```bash
python solution.py
```

---

## What This Project Demonstrates

This project shows how a purely random experiment can be used to estimate a fundamental mathematical constant.

It is a classic example of Monte Carlo methods and probabilistic computation.
