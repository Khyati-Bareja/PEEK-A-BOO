import random
import time
import os


class element:
    def __init__(self):
        self.value = 0
        #  to check if the element/cell has already been guessed or not
        self.checkGuess = 0


class Matrix:
    def __init__(self, grid_size):
        self.resultGrid = []
        self.grid_size = grid_size
        self.score = 0
        self.actual_guesses = 0
        self.cheated_guesses = 0
        self.flag1 = False
        self.create_grid(self.grid_size)
        self.choice = 4
        self.flag2 = 0
        self.minimum_possible_guesses = self.grid_size * self.grid_size / 2

    def create_grid(self, gridSize):
        if self.grid_size % 2 != 0:
            print("Invalid grid size")
            exit()
        TotalLst = gridSize * gridSize // 2
        lst = list(range(TotalLst)) * 2
        random.shuffle(lst)
        self.resultGrid = [[element() for j in range(gridSize)] for i in range(gridSize)]
        for i in range(gridSize):
            for j in range(gridSize):
                self.resultGrid[i][j].value = lst.pop()

    def display_grid(self, choice, row1, col1, row2, col2):

        print("    " + "   ".join(f"[{chr(65 + i)}]" for i in range(self.grid_size)))
        checkGuessSum = 0
        for i in range(self.grid_size):
            print("[" + str(i) + "] ", end="")
            for j in range(self.grid_size):
                checkGuessSum += self.resultGrid[i][j].checkGuess
                if choice == "3" or self.resultGrid[i][j].checkGuess:
                    print(self.resultGrid[i][j].value, end="     ")
                elif choice == "1" and ((i == row1 and j == col1) or (i == row2 and j == col2)):
                    print(self.resultGrid[i][j].value, end="    ")
                elif choice == "2" and (i == row1 and j == col1):
                    print(self.resultGrid[i][j].value, end="    ")
                else:
                    print("X", end="     ")
            print()

        # To compute the score
        if checkGuessSum == self.grid_size * self.grid_size:
            self.score = (self.minimum_possible_guesses / (self.actual_guesses + self.cheated_guesses)) * 100
            if choice == "3" and self.actual_guesses == 0 and self.cheated_guesses == 0:
                print("")
            elif self.actual_guesses == 0 and self.cheated_guesses > 2:
                print("")
                print("You cheated - Loser!. Your score is: 0!")
                print("")
            else:
                print("")
                print("Oh Happy Day. You've Won!! Your score is: " + str(int(self.score)))
                print("")
                self.flag2 = 1
                # self.flag1 = True

    def display_grid_with2val(self, row1, col1, row2, col2):

        print("     " + "   ".join(f"[{chr(65 + i)}]" for i in range(self.grid_size)))
        for i in range(self.grid_size):
            print("[" + str(i) + "] ", end="")

            for j in range(self.grid_size):
                if (i == row1 and j == col1) or (i == row2 and j == col2):
                    # if self.resultGrid[i][j].checkGuess:
                    # print("The cell has already been Guessed, Try guessing another cell!")
                    print(self.resultGrid[i][j].value, end="   ")
                else:
                    if self.resultGrid[i][j].checkGuess:
                        print(self.resultGrid[i][j].value, end="   ")
                    else:
                        print('X', end="   ")

            print()

    def uncoverOneElement(self, choice):
        # As using Option "2" counts to be equivalent to 2 guesses
        self.cheated_guesses += 2
        while True:
            val1 = input("Enter cell coordinates which you want to reveal: ")
            val1 = list(map(str, val1))

            col1 = ord(val1[0].upper()) - 65
            if len(val1) > 2 and self.grid_size <= 9:
                print("")
                print("Input error: row entry is out of range for this grid Or of Incorrect Type. Please try again.")
                print("")

            else:
                if val1[0].isdigit() or val1[1].isalpha():
                    print("")
                    print("Enter Valid Input Format for Row and Column. please try again.")
                    print("")
                else:
                    row1 = int(val1[1])
                    if row1 > (self.grid_size - 1) and col1 > (self.grid_size - 1):
                        print("")
                        print("Input error: row entry is out of range for this grid. Please try again.\n"
                              "\nInput error: column entry is out of range for this grid. Please try again.")
                        print("")
                    elif row1 > (self.grid_size - 1):
                        print("")
                        print("Input error: row entry is out of range for this grid. Please try again.")
                        print("")
                    elif col1 > (self.grid_size - 1):
                        print("")
                        print("Input error: column entry is out of range for this grid. Please try again.")
                        print("")

                    else:
                        break

        if len(val1) <= 2 and self.grid_size <= 9:
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    if i == row1 and j == col1:
                        if self.resultGrid[i][j].checkGuess:
                            print("")
                            print("The cell has already been Guessed, Try guessing another cell!")
                            print("")
                        else:
                            self.resultGrid[row1][col1].checkGuess = 1

            self.display_grid(choice, row1, col1, self.grid_size + 10, self.grid_size + 10)

    def compare_cells(self):

        self.actual_guesses += 1
        val1 = input("Enter cell coordinates (e.g., a0): ")
        val2 = input("Enter cell coordinates (e.g., a0): ")
        val1.upper()
        val2.upper()
        x = list(map(str, val1))
        y = list(map(str, val2))
        while True:
            if val1[0].isdigit() or val1[1].isalpha():
                print("")
                print("Enter Valid Input Format for Row and Column. Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            elif val2[0].isdigit() or val2[1].isalpha():
                print("")
                print("Enter Valid Input Format for Row and Column.  Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            elif len(val1) > 2 and self.grid_size <= 9:
                print("")
                print("Input error: row entry is out of range for this grid for cell. Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            elif len(val2) > 2 and self.grid_size <= 9:
                print("")
                print("Input error: row entry is out of range for this grid for cell. Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            elif int(x[1]) > (self.grid_size - 1) and ord(x[0]) > (65 + self.grid_size - 1):
                print("Input error: row entry is out of range for this grid. Please try again.\n"
                      "\nInput error: column entry is out of range for this grid. Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            elif int(x[1]) > (self.grid_size - 1) or int(y[1]) > (self.grid_size - 1):
                print("")
                print("Input error: row entry is out of range for this grid. Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            elif ord(x[0].upper()) - 65 > (self.grid_size - 1) or ord(y[0].upper()) - 65 > (self.grid_size - 1):
                # print(ord(x[0].upper()) - 65 +ord(y[0]) )
                print("")
                print("Input error: column entry is out of range for this grid. Please try again.")
                print("")
                val1 = input("Enter cell coordinates (e.g., a0): ")
                val2 = input("Enter cell coordinates (e.g., a0): ")
                val1.upper()
                val2.upper()
                x = list(map(str, val1))
                y = list(map(str, val2))
            else:
                break

        row1 = int(x[1])
        row2 = int(y[1])
        col1 = ord(x[0].upper()) - 65
        col2 = ord(y[0].upper()) - 65
        num1 = 0
        num2 = 0
        for i in range(self.grid_size):
            # print("[" + str(i) + "] ", end="")
            for j in range(self.grid_size):
                if (i == row1 and j == col1) and (i == row2 and j == col2):
                    if self.resultGrid[i][j].checkGuess:
                        print("The cell " + str(j) + str(i) + " has already been Guessed, Try Again!")
                else:
                    num1 = self.resultGrid[row1][col1].value
                    num2 = self.resultGrid[row2][col2].value

        if num1 == num2:
            print("Match found!")
            self.display_grid_with2val(row1, col1, row2, col2)

            self.resultGrid[row1][col1].checkGuess = 1
            self.resultGrid[row2][col2].checkGuess = 1


        else:
            self.display_grid_with2val(row1, col1, row2, col2)
            time.sleep(2)
            os.system("clear")
            self.display_grid(1, row1 + 10, col1 + 10, row2 + 10, col2 + 10)
