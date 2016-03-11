from sys import argv
script, row, column = argv
class ChessBoard(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = [[0 for i in xrange(self.column)] for j in xrange(self.row)]
        for i in range(0, self.row):
            for j in range(0, self.column):
                self.board[i][j] = "_"

#    def __init__(self):
#        self.row = 10
#        self.column = 10
    # print the current chessboard
    def print_test(self):
        if self.row == 0 or self.column == 0:
            pass
        else:
            for i in range(0, self.row, 1):
                temp_row = self.board[i][0]
                for j in range(1, self.column, 1):
                    temp_row += " "
                    temp_row += self.board[i][j]
                print temp_row

    # place a pawn on the board
    def put_pawn(self, pawn, position_x, position_y):
        if position_x < self.column and position_y < self.row:
            if pawn == 0:
                self.board[position_x][position_y] = "O"
            elif pawn == 1:
                self.board[position_x][position_y] = "X"
            else:
                print "unknown pawn type!"
        else:
            print "the position is out of boundary!"

    # find if anyone wins there
    def check_winner(self, number):
        # check the rows
        for i in range(self.row):
            temp_number = 0
            temp_pawn = "_"
            for j in range(self.column):
                if self.board[i][j] == "O":
                    if temp_pawn == "O":
                        temp_number += 1
                        if temp_number == number:
                            return temp_pawn
                    else:
                        temp_pawn = "O"
                        temp_number = 1
                elif self.board[i][j] == "X":
                    if temp_pawn == "X":
                        temp_number += 1
                        if temp_number == number:
                            return temp_pawn
                    else:
                        temp_pawn = "X"
                        temp_number = 1
                else:
                    temp_number = 0
                    temp_pawn = "_" 
        for 

        return "NO_WINNER"
    

break_line = "============================"

if row.isdigit() and column.isdigit():
    #test = ChessBoard()
    test = ChessBoard(int(row), int(column))
    test.print_test()
    print break_line
    test.put_pawn(1,1,1)
    test.print_test()
else:
    print "please enter an number!"
