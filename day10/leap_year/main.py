
def divisible_by_4(year):
    if year % 4 == 0:
        return True

def divisible_by_100(year):
    if year % 100 == 0:
        return True

def divisible_by_400(year):
    if year % 400 == 0:
        return True

def is_leap_year(year):
    if not divisible_by_4(year):
        return False
    elif divisible_by_4(year) and not divisible_by_100(year):
        return True
    elif divisible_by_4(year) and divisible_by_100(year) and  divisible_by_400(year):
        return True
    elif divisible_by_4(year) and divisible_by_100(year) and not divisible_by_400(year):
        return False

result = is_leap_year(2023)
print(result)






# year must be divisible by 4
#Year must not be divisible by 100, but if is divisible by 400 it's still a leap year

