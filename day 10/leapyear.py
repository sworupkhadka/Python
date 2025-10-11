
def is_leap_year(year):
    # A leap year is divisible by 4
    if year % 4 == 0:
        # Except if it is also divisible by 100
        if year % 100 == 0:
            # Unless it is also divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# ✅ Test cases
print(is_leap_year(2024))  # Expected output: True
print(is_leap_year(2025))  # Expected output: False
