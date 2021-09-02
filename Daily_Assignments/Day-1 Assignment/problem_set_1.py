"""
Finding biggest number
"""


def biggest(num_1, num_2, num_3, num_4):
    return max(num_1, num_2, num_3, num_4)


"""
Finding armstrong number
"""


def armstrong(num):
    sum_buffer = 0
    num_1 = num
    while num_1 > 0:
        buffer = num_1 % 10
        sum_buffer += (buffer*buffer*buffer)
        num_1 //= 10
    if sum_buffer == num:
        return "True"
    else:
        return "False"


"""
To find GCD/HCF of two numbers
"""


def gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    return gcd(num_2, num_1 % num_2)


"""
LCD without HCF/GCD
"""


def lcm(num_1, num_2):
    large = max(num_1, num_2)
    small = min(num_1, num_2)
    i = large
    while 1:
        if i % small == 0:
            return i
        i += large


"""
Type of triangle - equilateral, isosceles, scalene, right angled
"""


def triangle(side_1, side_2, side_3):
    sqr_1 = side_1*side_1
    sqr_2 = side_2*side_2
    sqr_3 = side_3*side_3
    if side_1 == side_2 == side_3:
        return "equilateral"
    elif (side_1 == side_2) or (side_3 == side_1):
        return "isoceles"
    elif sqr_1+sqr_2 is sqr_3 or sqr_3+sqr_2 is sqr_1 or sqr_1+sqr_3 is sqr_2:
        return "right-angled"
    else:
        return "scalene"


"""
Finding vowel and consonants
"""


def vowel_consonant(char):
    if char in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        return "Vowel"
    else:
        return "Consonant"


"""
Finding leap year
"""


def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return "True"
    else:
        return "False"


"""
Finding quadrant of points
"""


def quadrant(x_1, y_1):
    if x_1 > 0 and y_1 > 0:
        return 'Q1'
    elif x_1 < 0 and y_1 > 0:
        return 'Q2'
    elif x_1 < 0 and y_1 < 0:
        return 'Q3'
    else:
        return 'Q4'


"""
Arithmetic operation
"""


def calculator(num_1, num_2):
    choice = int(input())
    if choice == 1:
        return num_1+num_2
    elif choice == 2:
        return num_1-num_2
    elif choice == 3:
        return num_1*num_2
    elif choice == 4:
        return num_1//num_2
    else:
        return "Wrong Choice"
