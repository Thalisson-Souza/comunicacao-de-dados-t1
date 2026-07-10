# Line Coding Simulator

Implementation of a tool for visualizing and comparing line codes in data communication networks.

## Implemented Line Codes
- Manchester
- Manchester Diferencial
- NRZ-I
- NRZ-L
- AMI
- Pseudoternário
- CMI
- MLT-3
- 2B1Q

## How It Works

When the program is run, an interactive menu is displayed in the terminal. The user can choose a predefined bit sequence, generate a random 16-bit sequence, or manually enter the bits.

After that, one of the implemented line codes can be selected to visualize its corresponding signal in a graph. There is also a comparison mode that allows the user to choose two line codes and compare their signals, displaying information such as the number of transitions and the approximate average value.

### Features

- Visualize two different line codes using the same bit sequence.
- Test predefined, random, or manually entered sequences.
- Compare two encoding methods.
- Graphically observe changes in signal level over bit intervals.

## How to Run

### 1. Using a virtual environment (recommended)

- Windows
```bash
py -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

py main.py
```

- Linux/MacOS
```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 main.py
```

### 2. Without a virtual environment (global installation)
```bash
pip install -r requirements.txt

py main.py
```
