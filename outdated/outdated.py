import re

def is_valid_date(date):
    # Check if the date matches the month-day-year format
    if re.match(r"\d{1,2}/\d{1,2}/\d{4}$", date):
        month, day, year = map(int, date.split('/'))
        return 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999
    # Check if the date matches the Month day, year format
    elif re.match(r"^\w+ \d{1,2}, \d{4}$", date):
        month_name, day, year = re.split(r" |,", date, maxsplit=2)
        month = month_name.capitalize()
        return month in [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ] and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999
    else:
        return False

def convert_date(date):
    # Convert the date to the YYYY-MM-DD format
    if re.match(r"\d{1,2}/\d{1,2}/\d{4}$", date):
        month, day, year = map(int, date.split('/'))
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    elif re.match(r"^\w+ \d{1,2}, \d{4}$", date):
        month_name, day, year = re.split(r" |,", date, maxsplit=2)
        month = month_name.capitalize()
        month_number = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ].index(month) + 1
        return "{:04d}-{:02d}-{:02d}".format(int(year), month_number, int(day))

def main():
    while True:
        user_input = input("Enter a date (in month-day-year or Month day, year format): ").strip()
        if is_valid_date(user_input):
            converted_date = convert_date(user_input)
            print(converted_date)
            break
        else:
            print("Invalid date. Please try again.")

if __name__ == "__main__":
    main()
