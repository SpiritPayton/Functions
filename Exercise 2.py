def make_positive(number):
    abs_value = abs(number)
    return abs_value


# Main routine
number_to_check = int(input("Enter a number to check: "))
print(f"the absolute value of {number_to_check} is "
    f"{make_positive(number_to_check)}")
