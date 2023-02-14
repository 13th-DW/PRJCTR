import random


def recall_errorhandling_1():

    while True:
        try:
            input_number = int(input("Plese, enter an integer: "))
            print(input_number)
            break
        except ValueError:
            continue


def recall_errorhandling_2():

    try:
        input_str = input("Plese, enter a string: ")
        input_num = int(input("Plese, enter an integer: "))
        print(input_str[input_num])

    except ValueError:
        print("This is not a number")

    except IndexError:
        print("Index is out of range")


# updated
def election():
    number_of_voters = 10000

    num_of_regions = int(input("Enter number of regions: "))
    # Region rating
    reg_rat = []
    for i in range(num_of_regions):  # Here we collect all ratings from all regions
        region = int(
            input(f"Enter rating for 1st candidate in {i+1} region: "))
        reg_rat.append(region)

    reg_rat_voted = []
    # voting simulation
    for region in reg_rat:
        i = 0
        # can we use "for" w-out any actions with "vote"?
        for vote in range(number_of_voters):
            a = random.random()

            if a <= (region/100):
                i += 1

        reg_rat_voted.append(i)

    first_candidate_votes = sum(reg_rat_voted)
    second_candidate_votes = 0
    region_num = 1

    for i in reg_rat_voted:  # counting votes for the second candidate and announcement of the results
        print(
            f"Region {region_num}: {i} votes for 1st candidate, {number_of_voters - i} votes for 2nd candidate")
        second_candidate_votes += number_of_voters - i
        region_num += 1

    # Result
    if first_candidate_votes > second_candidate_votes:
        print(
            f"Result: 1st candidate won with {first_candidate_votes} votes and {first_candidate_votes/((first_candidate_votes+second_candidate_votes)/100):.2f}% of all votes")
    elif first_candidate_votes < second_candidate_votes:
        print(
            f"Result: 2nd candidate won with {second_candidate_votes} votes and {second_candidate_votes/((first_candidate_votes+second_candidate_votes)/100):.2f}% of all votes")


def tuple_of_int(tuple_: tuple) -> tuple:
    try:
        # updated
        results = min(tuple_), max(tuple_)
        return results
    except ValueError:
        return "ValueError: min() arg is an empty sequence"


def compute_difference(first: list, second: list) -> list:
    # but for more correct answer + [number_b for number_b in b if number_b not in a]
    return [first_number for first_number in first if first_number not in second]


# updated
def sum_of_two(nums: list, target: int) -> list:

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# updated
def unique_elements(arr: list) -> list:
    result = []
    cursed = []

    for i in arr:
        if i not in cursed:
            if i not in result:
                result.append(i)
            else:
                cursed.append(i)
                result.remove(i)

    if len(result) == len(arr):
        result.clear()

    return result, cursed


# updated
def odd_elements(arr: list) -> list:
    result = []

    for i in arr:
        if i not in result:
            result.append(i)
        else:
            result.remove(i)

    if len(result) == len(arr):
        result.clear()

    return result


# updated
def second_largest_element(arr: list) -> int:
    # sorting list
    arr.sort()

    if min(arr) == max(arr) or len(arr) < 2:
        return None
    elif arr.count(max(arr)) > 1:
        return arr[arr.index(max(arr)) + 1]
    elif arr.count(max(arr)) == 1:
        return arr[arr.index(max(arr)) - 1]


def cities():

    def population(e):
        return e[1]

    arr = [
        ('New York City', 8550405),
        ('Los Angeles', 3792621),
        ('Chicago', 2695598),
        ('Houston', 2100263),
        ('Philadelphia', 1526006),
        ('Phoenix', 1445632),
        ('San Antonio', 1327407),
        ('San Diego', 1307402),
        ('Dallas', 1197816),
        ('San Jose', 945942),
    ]

    arr.sort(key=population)

    a = 0
    total = 0

    while a < len(arr):
        total += arr[a][1]
        a += 1

    average = int(total / len(arr))

    return arr, total, average


def longest_increasing_sequence(arr: list) -> int:
    result = []
    a = 0
    b = 0

    for i in arr:
        if i > b:
            b = i
            a += 1

        result.append(a)

    return max(result)
