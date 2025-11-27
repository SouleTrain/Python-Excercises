def read_int(prompt, min, max):
    x = False
    while not x:
        try:
            value = int(input(prompt))
            x = True
        except ValueError:
            print("Error: Wrong Input")
        if x:
            x = value >= min and value <= max
        if not x:
            print("Number Not In Range (-10-10)")
    return value

v = read_int("Enter a number between -10 and 10: ", -10, 10)
print("Number Is", v)