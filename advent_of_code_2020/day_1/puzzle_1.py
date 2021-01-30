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
"""

import csv

TOTAL_TO_COMPARE = 2020

def evaluate_expense_report(expense_report_filename):
    expense_report_data = read_expense_report(expense_report_filename)
    cleaned_expense_report = clean_expense_report(expense_report_data)

    for i, value_1 in enumerate(cleaned_expense_report):
        value_to_find = TOTAL_TO_COMPARE-value_1
        for j, value_2 in enumerate(cleaned_expense_report[i+1:]):
            if value_2 == value_to_find:
                return value_1*value_2
    return None

def clean_expense_report(expense_report):
    return list(filter(lambda value: value<=TOTAL_TO_COMPARE, sorted(expense_report,reverse = True)))

def read_expense_report(expense_report_filename):
    data = []
    with open(expense_report_filename, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(int(line[0]))
    return data

if __name__ == '__main__':
    print(evaluate_expense_report('example.csv'))