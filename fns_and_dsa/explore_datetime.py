import datetime

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.datetime.now()
    print("Current date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print("furture date: ", future_date.strftime("%Y-%m-%d"))

