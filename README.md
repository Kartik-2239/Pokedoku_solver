# Pokedoku Solver

An automated solver for the [Pokedoku](https://pokedoku.com/) puzzle game using Google's Gemini AI.

## Overview

This tool automates solving Pokedoku puzzles by:
1. Capturing a screenshot of the puzzle grid
2. Using OCR to extract the constraints
3. Finding Pokemon that match the constraint pairs
4. Automatically entering the answers

## Requirements

- Python 3.x
- Chrome browser
- Google API keys for Gemini AI

## Installation

1. Clone this repository
   ```
   git clone https://github.com/Kartik-2239/Pokedoku_solver.git
   cd pokedoku-solver
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google API keys in the respective Python files

## Usage

Run the main script:
```
python main.py
```

The script will automatically:
- Open Chrome and navigate to Pokedoku
- Take a screenshot of the puzzle
- Process the constraints
- Find matching Pokemon
- Input the answers

## Files

- `main.py` - Main script that orchestrates the solving process
- `crop_img.py` - Functions to crop the screenshot to isolate the puzzle grid
- `ocr.py` - Functions for OCR and constraint extraction
- `Actual_answers.py` - Functions to find Pokemon matching the constraints

## Note

You may need to adjust the crop coordinates in `crop_img.py` depending on your screen resolution.
