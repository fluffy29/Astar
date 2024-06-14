# France Map A* Search

This project implements the A* search algorithm to find the shortest path between cities in France using a heuristic based on Euclidean distance. The cities and their coordinates are predefined, and the search algorithm uses a hash table to store city data.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [File Descriptions](#file-descriptions)
- [Acknowledgments](#acknowledgments)

## Introduction

The goal of this project is to implement the A* search algorithm to find the shortest path between two cities in France. The project includes:
- A hash table implementation to store city data.
- The A* search algorithm.
- A simple user interface to input the start and end cities.

## Prerequisites

To run this project, you need to have Python installed on your machine. This project is written in Python 3.

## Usage

1. **Run the script**:
    
    python Astar.py [start_city] [end_city]

    If you don't provide the `start_city` and `end_city` as command-line arguments, the script will prompt you to enter them.

2. **Example command**:

    python Astar.py Paris Marseille
  

3. **Ensure the map file**:
    Make sure the `FRANCE.MAP` file is in the same directory as `Astar.py`.

## Example

Here is an example of running the script:
```sh
$ python Astar.py Paris Marseille
Path found: ['Paris', 'Lyon', 'Marseille']
```
