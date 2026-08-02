# Django Piscine - 42

> This repository contains my work for the **42 Django Piscine**.
> The goal of the Piscine is to learn the fundamentals of Django by completing a series of projects, where each one introduces new concepts and builds on the previous exercises.

##  Django Piscine Roadmap

```mermaid
flowchart TB

    START([Start])

    START --> DAY0

    subgraph DAY0["Day 0 - Introduction"]
        direction TB
        D00["Django - 0 - Initiation"]
        D01["Django - 0 - Starting"]
        D02["Django - 0 - Oob"]

        D00 --> D01 --> D02
    end

    DAY0 --> DAY1

    subgraph DAY1["Day 1 - Web Applications"]
        direction TB
        D10["Django - 1 - Lib"]
        D11["Django - 1 - Base Django"]

        D10 --> D11
    end

    DAY1 --> DAY2

    subgraph DAY2["Day 2 - Database"]
        direction TB
        D20["Django - 2 - SQL"]
    end

    DAY2 --> DAY3

    subgraph DAY3["Day 3 - Advanced Concepts"]
        direction TB
        D30["Django - 3 - Sessions"]
        D31["Django - 3 - Advanced"]
        D32["Django - 3 - Final Project"]

        D30 --> D31 --> D32
    end

    DAY3 --> END([Piscine Complete])
```
## Validation

Projects **must be validated in order**. You cannot register for the next project until the previous one has been successfully validated.

The required validation order is:

<div align="center">
  <img 
    src="https://github.com/user-attachments/assets/df6eef51-ffd9-4d61-8799-3187fcb83d35"
    alt="Screenshot from 2025-11-23"
    style="width: 100%; max-width: 1200px; height: auto; border-radius: 8px;"
  />
</div>

## Repository

Each project is organized in its own directory and contains the corresponding solution for that exercise. This repository serves as a record of my progress throughout the Django Piscine.
