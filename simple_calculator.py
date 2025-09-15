#!/usr/bin/env python3
"""
Simple Calculator (CLI)

Usage:
  - Enter expressions in the form: <number> <operator> <number>
    Examples:
      2 + 3
      10 - 4.5
      7 * 8
      9 / 2
      9 // 2    
      10 % 3
      2 ** 8

  - Commands:
      help  -> show this help
      q     -> quit (also: quit, exit)

Notes:
  - Supports integers and decimals, including negatives
  - Gracefully handles division by zero and invalid inputs
"""

import re
from typing import Callable, Dict

# Map supported operators to their corresponding functions
OPS: Dict[str, Callable[[float, float], float]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '//': lambda a, b: a // b,
    '%': lambda a, b: a % b,
    '**': lambda a, b: a ** b,
}

# Regex to parse expressions like:  -12.5  **  3
EXPR_RE = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*(//|\*\*|[+\-*/%])\s*(-?\d+(?:\.\d+)?)\s*$")


def calculate_expression(expr: str) -> float:
    """Parse and evaluate a binary arithmetic expression.

    Supports: +, -, *, /, //, %, ** with floats and negatives.
    Raises ValueError for invalid formats or math errors.
    """
    m = EXPR_RE.match(expr)
    if not m:
        raise ValueError("Invalid format. Use: <number> <operator> <number> (try 'help')")

    a_str, op, b_str = m.groups()
    a = float(a_str)
    b = float(b_str)

    if op not in OPS:
        raise ValueError(f"Unsupported operator: {op}")

    # Handle division by zero cases explicitly for clarity
    if op in {'/', '//', '%'} and b == 0:
        raise ValueError("Division by zero is not allowed")

    return OPS[op](a, b)


def format_number(x: float) -> str:
    """Format numbers to avoid unnecessary trailing .0 for integers."""
    if x == int(x):
        return str(int(x))
    return str(x)


def print_help() -> None:
    print(__doc__)


def main() -> None:
    print("Simple Calculator - type 'help' for instructions, 'q' to quit.")
    while True:
        try:
            expr = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not expr:
            continue

        lower = expr.lower()
        if lower in {"q", "quit", "exit"}:
            print("Goodbye.")
            break
        if lower == "help":
            print_help()
            continue

        try:
            result = calculate_expression(expr)
            print("=", format_number(result))
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
