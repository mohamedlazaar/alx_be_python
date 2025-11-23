# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS    

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32

def main():
    temperature_to_convert = float(input("Enter the temperature to convert: "))  # Changed to float for decimal values
    conversion_type = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()
    
    if conversion_type == "C":
        converted_temp = celsius_to_fahrenheit(temperature_to_convert)
        print(f"{temperature_to_convert}°F is {converted_temp:.2f}°C")  # Fixed label
    elif conversion_type == "F":    
        converted_temp = fahrenheit_to_celsius(temperature_to_convert)
        print(f"{temperature_to_convert}°C is {converted_temp:.2f}°F")  # Fixed label
    else:
        print("Invalid conversion type. Please enter 'C' or 'F'.")

main()
