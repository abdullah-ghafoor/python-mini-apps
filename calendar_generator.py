import calendar

def display_calendar():
    year=int(input("Enter Year : "))
    month=int(input("Enter Month (1-12) : "))
    
    cal = calendar.TextCalendar(calendar.SUNDAY)

    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)
display_calendar()