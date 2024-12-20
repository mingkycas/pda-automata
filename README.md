# PDA String Validator and Visualizer

This project implements a Pushdown Automaton (PDA) to validate strings of the form `aⁿbⁿ` (where n ≥ 1) and provides a simple graphical user interface (GUI) to interact with the PDA. The application checks if the given string is accepted by the PDA and visualizes the PDA's state diagram.

## Features

- **PDA Simulation**: The PDA checks if the given string follows the pattern `aⁿbⁿ` where there are equal numbers of 'a' and 'b' characters.
- **GUI for Interaction**: A Tkinter-based graphical interface allows users to enter strings and view the validation result.
- **PDA Diagram**: The PDA's state diagram is drawn dynamically using Tkinter's Canvas widget, visually representing the transitions between states.

## How to Run

1. **Requirements**:  
   - Python 3.x
   - Tkinter (usually comes pre-installed with Python)

2. **Steps to Run**:
   - Clone the repository or download the script file.
   - Install Python 3.x if it's not already installed.
   - Run the `main()` function in the script to start the GUI.

   ```bash
   python pda_validator.py
