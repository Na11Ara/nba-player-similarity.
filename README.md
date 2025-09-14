# 🏀 NBA Player Similarity (2024–25 Season)

This project implements a **Player Similarity Tool** for the NBA 2024–25 season.  
Given a player’s name, it finds the **most statistically similar players** based on core performance metrics (Points, Rebounds, Assists).  

The focus of this project is not just on the results, but on **clean, maintainable, and testable code** — following software engineering principles such as modular design, type safety, and unit testing. This aligns with modern **Machine Learning Engineering practices** where code quality and reproducibility matter as much as model accuracy.

---

## 🚀 Features
- Loads player stats from a JSON dataset (best statistical player from all 30 NBA teams in the 2024–25 season).  
- Preprocesses numeric features with **min–max normalization** for fair comparison.  
- Computes **cosine similarity** between players.  
- Retrieves the **Top-K most similar players** to any given player.  
- Includes **unit tests** (with `pytest`) for data loading and similarity calculations.  
- Modular code structure with type annotations and docstrings for readability.  

---

## 📂 Project Structure
nba-player-similarity/
├── data/
│ └── players.json # Dataset with best player stats from all 30 teams
├── src/
│ ├── data_loader.py # Load and parse data
│ ├── preprocess.py # Data preprocessing & normalization
│ ├── similarity.py # Similarity calculations
│ └── main.py # Entry point (command-line tool)
├── tests/
│ ├── test_data_loader.py # Unit tests for data loader
│ └── test_similarity.py # Unit tests for similarity functions
│ └── conftest.py
├── README.md # Project documentation


## Usage

