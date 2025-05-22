def is_leap(year):
    # Check if year is divisible by 4 and not divisible by 100,
    # unless it's also divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap(year):
    leap = False
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
