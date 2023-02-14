# Update 24.01 01:28:

# Added parameters to the functions
# Temporary variables now called "temp"
# Fixed typo "answear" on line 45
# Removed parentheses for "if" conditions
# Removed abs() on line 84

# For fifth_program() have one strange issue, when I try to reverse 900 the program returns to me just 9. I think it's inpossible to retun 009 w-out str. Isn't it?

def first_program(first, second):

    first, second = second, first
    print("1. x, y = y, x\nNow x = " + str(first) + ", y = "+str(second))

    temp = first
    first = second
    second = temp
    print("2. With temporary variable:\n", "a = x\n", "x = y\n", "y = a")
    print("Now x = " + str(first) + ", y = "+str(second))

    first = first + second
    second = first - second
    first = first - second
    print("3. By arithmetic operations:\n",
          "x = x + y\n", "y = x - y\n", "x = x - y")
    print("Now x = " + str(first) + ", y = "+str(second))


def second_program(first, second):
    print("Difference is", abs(first - second))


def third_program(first, second):
    print("Maximum is:", max(first, second))


def fourth_program(number):
    number = number % 1000
    number = number // 100
    print("Middle digit is", number)


def fifth_program(number):
    # for more longer numbers will better to use loops)
    answer = 0

    temp = number % 10
    answer = (answer + temp) * 10
    number = number // 10
    temp = number % 10
    answer = (answer + temp) * 10
    number = number // 10
    answer += number
    print("Reversed number is", answer)


print("Hi, this is little console homework program) \nPlease choose from what exercise you want to start:\n1.Program that swaps values\n2.Difference between 2 numbers\n3.Biggers number\n4.'Find middle digit' program\n5.Exercise with asterlink)\n")
while True:
    startpoint = abs(int(input("1/2/3/4/5: ")))
    print('Good choise!')

    if startpoint == 1 or startpoint == 2 or startpoint == 3:

        first = int(input('Please, enter the first number: '))
        second = int(input('Please, enter the second number: '))

        if startpoint == 1:
            print('')
            print('1.Program that swaps values')
            first_program(first, second)

        elif startpoint == 2:
            print('')
            print('2.Difference between 2 numbers')
            second_program(first, second)

        elif startpoint == 3:
            print('')
            print('3.Biggers number')
            third_program(first, second)

    elif startpoint == 4 or startpoint == 5:
        print("For more longer numbers will better to use loops, but this time I got it by newline operations)")
        number = int(input('Please, enter the number: '))

        if startpoint == 4:
            print('')
            print("4.'Find middle digit' program")
            fourth_program(number)

        elif startpoint == 5:
            print('')
            print("5.*'Reverse the number by using math only & w-out str()'")
            fifth_program(number)

    else:
        print("Soppy, I don't understend. Please, choose one of the bottom.")
        continue

    another_one = input("Do you want to check another one? Y/n: ")

    if another_one == "Y" or another_one == "y":
        continue
    elif another_one == "N" or another_one == "n":
        print("See ya.")
        break
    else:
        print("OK, I think you want to continue) Please choose one of the bottom)\n..we both can play in this game..)")
        continue
