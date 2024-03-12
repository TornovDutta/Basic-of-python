day = "Monday"

match day:
    case "Monday":
        print("Today is Monday.")
    case "Tuesday":
        print("Today is Tuesday.")
    case "Wednesday":
        print("Today is Wednesday.")
    case "Thursday":
        print("Today is Thursday.")
    case "Friday":
        print("Today is Friday.")
    case "Saturday":
        print("Today is Saturday.")
    case "Sunday":
        print("Today is Sunday.")
    case _:
        print("That is not a valid day of the week.")