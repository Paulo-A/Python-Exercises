"""
--- Day 3: Toboggan Trajectory ---
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

SLOPE = [[1, 1],[3, 1], [5,1], [7,1], [1,2]]

class ForestMap(list):
    def __init__(self, filename):
        self.__read_txt(filename)
        self.__x_length()
        self.__y_length()

    def __read_txt(self, filename):
        with open(filename, 'r', newline='') as f:
            reader = f.read()
            if reader:
                self.data = list(reader.split('\n'))
            else:
                raise ValueError('Forest map cannot be empty')

    def __x_length(self):
        self.x_length = len(self.data[0])

    def __y_length(self):
        self.y_length = len(self.data)


    def trees_encountered(self, slope):
        number_of_encounters = 0
        x = self.__get_start_x()
        for y in range(0, self.y_length, slope[1]):
            rel_x = x-int(x/self.x_length)*self.x_length
            if self.data[y][rel_x] == '#':
                number_of_encounters += 1
            x+=slope[0]
        return number_of_encounters

    def __get_start_x(self):
        return self.data[0].find('.')

if __name__ == '__main__':
    forest_map = ForestMap('example.txt')
    total_trees_encountered = 1
    for slope in SLOPE:
        total_trees_encountered *= forest_map.trees_encountered(slope)
    print(total_trees_encountered)
