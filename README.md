# Ant Colony Optimization for TSP

This project implements an Ant Colony Optimization (ACO) algorithm to solve the Traveling Salesman Problem (TSP) using Python.

## Description

The algorithm simulates the behavior of ants searching for the shortest path between cities. It uses pheromone trails and visibility (inverse of distance) to probabilistically choose the next city to visit. Over multiple iterations, the pheromone trails are updated based on the quality of the solutions found, guiding the ants towards better solutions.

## Files

- `genitique.py`: The main script containing the implementation of the ACO algorithm.

## Dependencies

- `numpy`
- `random`

You can install the required dependencies using pip:

```bash
pip install numpy
```

```
python genitique.py
```
