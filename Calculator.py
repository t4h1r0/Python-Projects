"""
Command-Line Calculator
Supports basic operations, history, and chained calculations.
"""

import math
import operator

# Operations 

def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):      return a ** b
def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b
def sqrt(a):          return math.sqrt(a)

BINARY_OPS = {
    "+":  (add,      "Addition"),
    "-":  (subtract, "Subtraction"),
    "*":  (multiply, "Multiplication"),
    "/":  (divide,   "Division"),
    "**": (power,    "Power"),
    "%":  (modulo,   "Modulo"),
}

UNARY_OPS = {
    "sqrt": (sqrt, "Square Root"),
}

# Helpers 

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ✗ Invalid number. Please try again.")

def format_result(n):
    """Show integers cleanly, floats with up to 10 decimal places."""
    if n == int(n) and abs(n) < 1e15:
        return str(int(n))
    return f"{n:.10g}"

def print_menu():
    print("\n" + "─" * 40)
    print("  CALCULATOR")
    print("─" * 40)
    print("  Binary operations:")
    for sym, (_, name) in BINARY_OPS.items():
        print(f"    {sym:>4}  {name}")
    print("\n  Unary operations:")
    for sym, (_, name) in UNARY_OPS.items():
        print(f"    {sym:>4}  {name}")
    print("\n  Commands:   H  History   C  Clear   Q  Quit")
    print("─" * 40)

# Main Loop 

def main():
    history = []
    last_result = None

    print("\n╔══════════════════════════════════════╗")
    print("║   Welcome to the Python Calculator   ║")
    print("╚══════════════════════════════════════╝")
    print("  Type 'menu' to see all operations.")
    print("  Tip: Start a number with '=' to reuse the last result.")

    while True:
        try:
            print()
            op = input("  Operation: ").strip().lower()

            if op in ("q", "quit", "exit"):
                print("\n  Goodbye!\n")
                break

            elif op in ("h", "history"):
                if not history:
                    print("  No history yet.")
                else:
                    print("\n  ─── History ───")
                    for i, entry in enumerate(history, 1):
                        print(f"  {i:>3}. {entry}")
                continue

            elif op in ("c", "clear"):
                history.clear()
                last_result = None
                print("  History cleared.")
                continue

            elif op in ("menu", "m", "help"):
                print_menu()
                continue

            elif op in UNARY_OPS:
                fn, name = UNARY_OPS[op]
                a = get_number("  Number: ")
                result = fn(a)
                expr = f"{op}({format_result(a)}) = {format_result(result)}"
                history.append(expr)
                last_result = result
                print(f"\n   {format_result(result)}")

            elif op in BINARY_OPS:
                fn, name = BINARY_OPS[op]

                raw_a = input("  First number (or '=' for last result): ").strip()
                if raw_a == "=" and last_result is not None:
                    a = last_result
                    print(f"     Using {format_result(a)}")
                else:
                    try:
                        a = float(raw_a)
                    except ValueError:
                        print("  Invalid number.")
                        continue

                raw_b = input("  Second number (or '=' for last result): ").strip()
                if raw_b == "=" and last_result is not None:
                    b = last_result
                    print(f"     Using {format_result(b)}")
                else:
                    try:
                        b = float(raw_b)
                    except ValueError:
                        print("  Invalid number.")
                        continue

                result = fn(a, b)
                expr = f"{format_result(a)} {op} {format_result(b)} = {format_result(result)}"
                history.append(expr)
                last_result = result
                print(f"\n   {format_result(result)}")

            else:
                print(f"  Unknown operation '{op}'. Type 'menu' for help.")

        except ValueError as e:
            print(f"  Error: {e}")
        except KeyboardInterrupt:
            print("\n\n  Goodbye!\n")
            break

if __name__ == "__main__":
    main()