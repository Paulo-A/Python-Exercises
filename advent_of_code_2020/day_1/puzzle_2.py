"""
--- Day 1: Report Repair ---
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

import csv

TOTAL_TO_COMPARE = 2020

def evaluate_expense_report(expense_report_filename):
    expense_report_data = read_expense_report(expense_report_filename)
    cleaned_expense_report = clean_expense_report(expense_report_data)

    for i, value_1 in enumerate(cleaned_expense_report):
        for j, value_2 in enumerate(cleaned_expense_report[i+1:]):
            value_to_find = TOTAL_TO_COMPARE-value_1-value_2
            for k, value_3 in enumerate(cleaned_expense_report[j+1:]):
                if value_3 == value_to_find:
                    return value_1*value_2*value_3
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