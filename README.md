# Word Permutations and Combinations Generator

This script is intended for generating a wordlist based on some specific words.

## Features

- Generate permutations and combinations of words.
- Insert specified symbols into words at all possible or user-defined positions.
- Output results to a file or print to console.

## Requirements

- Python 3.x

## Usage

### Command-Line Arguments

- `-w, --wordsfile`: File containing words, one per line.
- `-p, --permutations`: Comma-separated words (spaces allowed).
- `-min, --minlen`: Minimum length of combinations (default: 1).
- `-max, --maxlen`: Maximum length of combinations.
- `-o, --output`: Output file to save results.
- `-s, --symbols`: Symbols to insert into words.
- `--positions`: Comma-separated list of positions (0-based) to insert symbols.

### Examples

1. python3 mycrunch.py -w words.txt -min 1 -max 1 -s @#$ --positions 0,2 -o output.txt
2. python3 mycrunch.py -p alex, 3234, boom, 2004, aflek_justin -min 2 -max 5 -s @^&

> This project is inspired by crunch and a simpler version of it for this specific use
