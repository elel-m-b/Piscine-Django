# Django Piscine - 42

> This repository contains my work for the **42 Django Piscine**.
> The goal of the Piscine is to learn the fundamentals of Django by completing a series of projects, where each one introduces new concepts and builds on the previous exercises.
## 🗺️ Piscine Structure

```mermaid
flowchart LR

    START([🚀 Start])

    subgraph D0["📅 Day 0 - Django Basics"]
        D00["Initiation"]
        D01["Starting"]
        D02["Oob"]
    end

    subgraph D1["📅 Day 1 - Building Apps"]
        D10["Lib"]
        D11["Base Django"]
    end

    subgraph D2["📅 Day 2 - Database"]
        D20["SQL"]
    end

    subgraph D3["📅 Day 3 - Advanced"]
        D30["Sessions"]
        D31["Advanced"]
        D32["Final Project"]
    end

    START --> D00
    D00 --> D01
    D01 --> D02

    D02 --> D10
    D10 --> D11

    D11 --> D20

    D20 --> D30
    D30 --> D31
    D31 --> D32

    D32 --> END([🎓 Piscine Complete])
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
