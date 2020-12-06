"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

To begin, get your puzzle input.
"""

expenses = [int(line.rstrip('\n')) for line in open('./input.txt')]
expenses.sort()

middle = round(len(expenses) / 2)
iterationIndex = 0
solution = None

for expense in expenses:
    # if current place 1/2 through sorted list is greater then we only worry about numbers below that
    if (expense + expenses[middle]) > 2020:
        while iterationIndex < middle:
            if (expense + expenses[iterationIndex]) == 2020:
                solution = expense * expenses[iterationIndex]
                break
            iterationIndex += 1

    elif (expense + expenses[middle]) == 2020:
        solution = expense * expenses[middle]
        break
    else:
        iterationIndex = middle
        while iterationIndex < len(expenses):
            if (expense + expenses[iterationIndex]) == 2020:
                solution = expense * expenses[iterationIndex]
                break
            iterationIndex += 1

print("Solution: ", solution)



