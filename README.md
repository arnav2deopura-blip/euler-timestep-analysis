# The Effect of Timestep Size on the Accuracy of Euler's Method in Simulating Free-Fall Motion

This repository contains a computational physics study analyzing the truncation error inherent in first-order numerical approximations using a free-fall simulation framework.

## Project Structure
* `free_fall_simulation.py`: Python script utilizing NumPy and Matplotlib to run the simulation and calculate mean/max error data.
* `freefall_paper.pdf`: The final, compiled academic manuscript detailing the results.
* `latex_source/`: Raw LaTeX (`.tex`) and BibTeX (`.bib`) files used to generate the manuscript.
* `figures/`: All the figures that were used in the final paper.

## Main Findings
This project confirms the nature of Euler's method as a first-order numerical approximation. By testing multiple configurations, the data demonstrates that the cumulative global error accumulates linearly and is directly proportional to the chosen timestep size ($\Delta t$) when compared against the exact analytical solution.

## Visualizing the Convergence
| Timestep (s) | Mean Error (m) | Max Error (m) |
|---|---|---|
| 0.01 | 0.1113 | 0.2222 |
| 0.05 | 0.5641 | 1.1159 |
| 0.10 | 1.1527 | 2.2563 |
| 0.50 | 6.7444 | 12.2625 |
| 1.00 | 17.1675 | 29.4300 |

## Requirements
* Python 3.12
* NumPy
* Matplotlib

## Usage
1. Clone the repository.
2. Run the simulation script:
   ```bash
   python free_fall_simulation.py
3. Enter your desired time step when prompted in the terminal to view the resulting trajectory and error tracking plots.
