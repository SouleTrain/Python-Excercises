def is_year_leap(year):
        # Calculations For Leap Year
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 4 == 0 and year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
            print("OK")
    else:
            print("Failed")

def days_in_month(year, month):
    for days in range(0, 12):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month > 8 and month % 2 != 0:
            var = 30
            return var
        if month == 2 and is_year_leap(year) == True:
            var = 29
            return var
        elif month == 2 and is_year_leap(year) == False:
            var = 28
            return var
    else:
        var = 31
        return var



test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")