class FormulaError(Exception):
    def __init__(self, message="Invalid formula format"):
        self.message = message
        super().__init__(self.message)

class WrongOperatorError(Exception):
    def __init__(self, message="Invalid operator"):
        self.message = message
        super().__init__(self.message)

attempts = 3

while attempts > 0:
    try:
        formula = input("Enter a formula with spaces (e.g., 2 * 5): ")
        elements = formula.split()

        if len(elements) != 3:
            raise FormulaError("Formula must consist of three elements")

        num1 = float(elements[0])
        operator = elements[1]
        num2 = float(elements[2])

        if operator not in ("*", "/"):
            raise WrongOperatorError("Invalid operator. Use '*' or '/'")

        if operator == "/" and num2 == 0:
            raise ZeroDivisionError("Can't divide by zero")

    except FormulaError as e:
        print(f"Formula Error: {e}")
    except WrongOperatorError as e:
        print(f"Operator Error: {e}")
    except ZeroDivisionError as e:
        print(f"Zero Division Error: {e}")
    except ValueError:
        print("Value Error: Entered numbers must be float")

    else:
        if operator == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        print(f"Result: {result:.2f}")
        break

    finally:
        attempts -= 1
        if attempts > 0:
            print(f"Remaining attempts: {attempts}")
        else:
            print("No more attempts. Exiting.")
