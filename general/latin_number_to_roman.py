class LatinNumberToRoman:
    def __init__(self):
        self.__constructor = {
            'letters': [['M','',''],['C', 'D', 'M'],['X','L', 'C'],['I', 'V', 'X']],
            'default_base': [[],[0],[0,0],[0,0,0],[0,1],[1],[1,0],[1,0,0],[1,0,0,0],[0,2]]
        }

    def convert(self, num):
        self.latin = num
        self.converted = ''

        if num<=0:
            raise ValueError('Cannot convert zero or negative numbers')
        elif num>3999:
            raise ValueError('Cannot convert numbers greater than 3999')
        elif num <= 3999:
            decimal_base = [1000, 100, 10, 1]

            for i in range(len(decimal_base)):
                div = int(num/decimal_base[i])
                rest_div = num % decimal_base[i]
                for number in self.__constructor['default_base'][div]:
                    self.converted += self.__constructor['letters'][i][number]
                num=rest_div

            print('Number converted from latin numeral to roman:\n', self.latin, '->', self.converted)


if __name__ == '__main__':
    roman = LatinNumberToRoman()
    roman.convert(1490)