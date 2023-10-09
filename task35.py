day = input("What day is today:")
if day == "Monday" or "Tuesday" or "Wednesday" or "Thursday":
    print("weekday")
elif day == "Friday":
    print("TGIF")
elif day == "Saturday" or "Sunday":
    print("weekend")
else:
    print("invalid input")