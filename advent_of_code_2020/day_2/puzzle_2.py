"""
--- Day 2: Password Philosophy ---
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

import csv

STRING_TO_REPLACE_DATABASE = ['-', ': ', ' ']

class Database(list):
    def __init__(self, csv_filename):
        self.__read_csv(csv_filename)
        self.__clean()

    def __clean(self, ):
        clean_data = []
        for row in self.data:
            for string in STRING_TO_REPLACE_DATABASE:
                row = row.replace(string, ',')
            row = list(row.split(','))
            clean_data.append([int(row[0]), int(row[1]), row[2], row[3]])
        self.data = clean_data

    def __read_csv(self, filename):
        self.data = []
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.data.append(line[0])

    def evaluate_data(self):
        number_of_occurences = 0
        for row in self.data:
            if (row[3][row[0]-1] == row[2]) != (row[3][row[1]-1] == row[2]):
                number_of_occurences += 1
        return number_of_occurences

if __name__ == '__main__':
    database = Database('example.csv')
    print(database.evaluate_data())