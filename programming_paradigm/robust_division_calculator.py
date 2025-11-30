def safe_divide(numerator, denominator):
    try:
        # Attempt division
        result = numerator / denominator
        return f"The result is {result:2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
