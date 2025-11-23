from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print("Current date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # return for later use


def calculate_future_date(current_date):
    """Calculates and displays a future date."""
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


# --- Program Execution ---
current_date = display_current_datetime()
calculate_future_date(current_date)
