from datetime import datetime
def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        time_difference = current_date - input_date
        return time_difference.days
    except ValueError:
        return "Please enter date in format: YYYY-MM-DD"
print(get_days_from_today(input(str('Enter date:'))))