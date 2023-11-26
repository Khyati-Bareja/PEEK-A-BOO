from grid import Matrix
import sys
import os

def titlebar(self):
    print("----------------------")
    print("|   PEEK-A-BOO       |")
    print("---------------------- \n")


def menu(self):
    print("\nMenu:")
    print("1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New game")
    print("5. Exit")

def play(self):

    titlebar(self)

    self.display_grid(self.choice, grid_size + 10, grid_size + 10, grid_size + 10, grid_size + 10)
    if not self.flag1:
        menu(self)
    else:
        print("4. New game")
        print("5. Exit")



    while True:

        choice = input("Select: ")
        if self.flag1 and choice != "4" and choice != "5":
            os.system("clear")
            titlebar(self)
            print("Invalid Input")
            menu(self)
            print("Matrix already revealed. Please start a new game or Exit!")
            print("")

        else:
            if choice == "1":
                os.system("clear")
                if self.flag2 == 1:
                    titlebar(self)
                    print("You have Already Won. Please Start a New Game or Exit.")
                    print("")
                    menu(self)
                else:
                    self.compare_cells()
                    play(game)

            elif choice == "2":
                os.system("clear")
                if self.flag2 == 1:
                    titlebar(self)
                    print("You have Already Won. Please Start a New Game or Exit.")
                    print("")
                    menu(self)
                else:
                    self.uncoverOneElement(choice)
                    play(game)
                    print("")
            elif choice == "3":
                os.system("clear")
                self.flag1 = True
                self.score = 0
                titlebar(self)
                if self.flag2 == 1:
                    print("You have Already Won. Please Start a New Game or Exit.")
                    print("")
                    menu(self)

                else:
                    self.display_grid(choice, grid_size + 10, grid_size + 10, grid_size + 10, grid_size + 10)
                    print("")
                    print("You cheated - Loser!. Your score is "+str(self.score)+"!")
                    print("")
                    menu(self)

                self.actual_guesses = 0


            elif choice == "4":
                os.system("clear")
                self.flag2 = 0
                self.actual_guesses = 0
                self.cheated_guesses= 0
                self.flag1 = False
                self.create_grid(self.grid_size)
                play(game)
                self.score = 0


            elif choice == "5":
                os.system("clear")
                self.flag2 = 0
                self.score = 0
                self.actual_guesses = 0
                exit()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(" Please run the File in format similar to : python3 grid.py <grid_size>")
        sys.exit(1)

    grid_size = int(sys.argv[1])
    game = Matrix(grid_size)
    play(game)
