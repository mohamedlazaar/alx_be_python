from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print("Current date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

    number_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = current_date + timedelta(days=number_of_days)
    print("future date:", future_date.strftime("%Y-%m-%d"))
