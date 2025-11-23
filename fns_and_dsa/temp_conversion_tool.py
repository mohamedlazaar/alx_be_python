FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS    
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32

def main ():
    tempreture_to_convert = int(input("Enter the temperature to convert: "))
    conversion_type = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()
    if conversion_type == "C":
        converted_temp = celsius_to_fahrenheit(tempreture_to_convert)
        print(f"{tempreture_to_convert}°C is {converted_temp:.2f}°F")
    elif conversion_type == "F":    
        converted_temp = fahrenheit_to_celsius(tempreture_to_convert)
        print(f"{tempreture_to_convert}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid conversion type. Please enter 'C' or 'F'.")

main()
