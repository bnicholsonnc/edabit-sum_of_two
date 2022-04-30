#
# Benjamin Nicholson
# edabit.com challenge "Return the Sum of Two Numbers"
# https://edabit.com/challenge/rZToTkR5eB9Zn4zLh
# ©Apr 30, 2022
#
# define function to add two numbers
def sum_of_two(num1, num2):
    result = num1 + num2
    return result


# main program gets two integers from user and pass them to sum_of_two function
def main():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = sum_of_two(num1, num2)
    print(f'The sum of {num1} and {num2} is {result}.')


main()
