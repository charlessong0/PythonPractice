class chessboard(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column

#    def __init__(self):
#        self.row = 10
#        self.column = 10

    def print_test(self):
        if self.row == 0 or self.column == 0:
            pass
        else:
            for i in range(0, self.column, 1):
                temp_row = "_"
                for j in range(0, self.row, 1):
                    temp_row += " _"
                print temp_row

#test = chessboard()
test = chessboard(5,5)
test.print_test()

