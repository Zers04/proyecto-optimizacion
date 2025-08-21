# 🎶 Optimization Project: Where Should I Place My Concert?

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/Zers04/proyecto-optimizacion/blob/main/README.md)
[![es](https://img.shields.io/badge/lang-es-blue.svg)](https://github.com/Zers04/proyecto-optimizacion/blob/main/README-es.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![MiniZinc](https://img.shields.io/badge/Modelado-MiniZinc-purple)

This project addresses a **discrete optimization problem**: determining the fairest location to hold a concert within the department of **Valle del Cauca**, avoiding favoring one city over another.

The problem is modeled on an **N x N**, where each city has integer coordinates, and the solution must ensure an equitable distribution of distances using the **Manhattan distance**.

---

## 📖 Problem Description

- The concert **cannot be held at the same location as any city**.
- The goal is to find a location such that:
  - The difference between the closest and farthest city to the concert is **≤ 2 km**.
  - The **maximum (Manhattan) distance** between the concert and any city is **minimized**.

---

## 🧮 Mathematical Model

**Objective Function**  
Objective Function

```
min ( max di ) donde di = |x - xi| + |y - yi|
```

**Main Constraints**
1. The concert cannot be placed at the same coordinates as a city. 
2. The difference between the closest and farthest city must be ≤ 2 km. 
3. The limits of the \(N \times N\) plane must be respected..  

---

## 💻 Implementation

The project was developed in **Python** with the following components:

- **Tkinter GUI**: interface to input data (N, number of cities, and their coordinates).
- **Procesamiento**: input validation and constraint verification.
- **Generación de código MiniZinc**: the system does not directly solve the problem, but **generates the MiniZinc model code**, ready to be executed in the corresponding IDE.

Example of expected input in the interface:

```
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
```

## 🚀 Installation and Run

### 1. Clone the repository
```bash
git clone https://github.com/Zers04/proyecto-optimizacion.git
cd proyecto-optimizacion
```

To start the project, run:

```bash
python main.py
```

## Authors ✒️

* **Juan David Cataño** - [Zers04](https://github.com/Zers04)
* **Valentina Londoño** - [Valtimore](https://github.com/valtimore)

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.