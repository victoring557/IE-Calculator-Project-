def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """subtracts the second number from the first"""
    return a - b


def multiply(a: float, b: float) -> float:
    """multiplies both numbers"""
    return a * b


def divide(a: float, b: float) -> float:
    """divides a by b. errors if b is 0"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def percentage_change(new: float, old: float) -> float:
    """how much it changed from old to new"""
    if old == 0:
        raise ValueError("Cannot divide by zero.")
    return (new - old) / old


def compound_growth(start: float, rate: float, periods: float) -> float:
    """grows the starting amount. 0.05 means 5 percent"""
    return start * (1 + rate) ** periods


def main():
    while True:
        choice = input("1 add, 2 subtract, 3 multiply, 4 divide, 5 percent, 6 growth, 7 quit: ")
        if choice == "7":
            break

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            if choice == "1":
                print(add(a, b))
            elif choice == "2":
                print(subtract(a, b))
            elif choice == "3":
                print(multiply(a, b))
            elif choice == "4":
                print(divide(a, b))
            elif choice == "5":
                print(percentage_change(a, b))
            elif choice == "6":
                periods = float(input("Periods: "))
                print(compound_growth(a, b, periods))
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
