# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    print("Temperature Conversion Tool")
    print("----------------------------")
    
    # Prompt the user for temperature
    temp_input = input("Enter the temperature value: ")

    # Validate numeric input
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt for unit (C or F)
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Conversion logic
    if unit == "C":
        result = convert_to_fahrenheit(temp_value)
        print(f"\n{temp_value}°C is equal to {result:.2f}°F")
    elif unit == "F":
        result = convert_to_celsius(temp_value)
        print(f"\n{temp_value}°F is equal to {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# Run program
if __name__ == "__main__":
    main()
