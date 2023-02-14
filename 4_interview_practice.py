from math import sqrt
from math import log2


# Name: Determine Color of a Chessboard Square
# Link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/

def squareIsWhite(self, coordinates: str) -> bool:
    let_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8']

    # 1 = black, 0 = white
    col = 0

    let_index = let_list.index(coordinates[0])
    num_index = num_list.index(coordinates[1])

    if (let_index + 1) % 2 != 0:
        col += 1
    if num_index % 2 != 0 and col == 0:
        col += 1
    elif num_index % 2 != 0 and col != 0:
        col -= 1

    return col == 0


# Name: Count Square Sum Triples
# Link: https://leetcode.com/problems/count-square-sum-triples/

def countTriples(self, n: int) -> int:
    ans = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            square = sqrt(i * i + j * j)
            if int(square) == square and square <= n:
                ans += 2

    return ans


# Name: Determine Color of a Chessboard Square
# Link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/

def isThree(self, n: int) -> bool:
    counter = []

    for i in range(1, n+1):
        if n % i == 0:
            counter.append(i)

    return len(counter) == 3


# Name: Add Digits
# Link: https://leetcode.com/problems/add-digits/description/

def addDigits(self, num: int) -> int:
    while num > 9:
        num = sum(map(int, str(num)))

    return num


# Name: Power of Two
# Link: https://leetcode.com/problems/power-of-two/

def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and log2(n) == int(log2(n))
