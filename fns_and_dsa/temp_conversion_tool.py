FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR    

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature_to_convert = float(input("Enter the temperature to convert: "))
    conversion_type = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()
    
    if conversion_type == "C":
        converted_temp = celsius_to_fahrenheit(temperature_to_convert)
        print(f"{temperature_to_convert}°F is {converted_temp:.2f}°C")
    elif conversion_type == "F":    
        converted_temp = fahrenheit_to_celsius(temperature_to_convert)
        print(f"{temperature_to_convert}°C is {converted_temp:.2f}°F")
    else:
        print("Invalid conversion type. Please enter 'C' or 'F'.")

main()