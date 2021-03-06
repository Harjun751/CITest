import pickle

# hi2


def init_game():
    game_board = [
        # e.g. ['SHP','FAC','BCH','HWY']
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
    ]
    # Building name:count of buildings
    building_pool = {
        "HSE": 8,
        "FAC": 8,
        "SHP": 8,
        "HWY": 8,
        "BCH": 8
    }
    return game_board, building_pool

# UI for in-game menu


def game_menu(game_board, building_pool):
    # implement auto Turn counter
    print("\nTurn Counter")

    # implement display game board
    print("Board")

    # in-game menu
    print("1. Build random building")
    print("2. Build random building")
    print("3. See remaining buildings")
    print("4. See current score")
    print("\n5. Save game")
    print("0. Exit to main menu")
    try:
        choice = int(input("Your choice? "))
        if choice == 1:
            # code to add random building 1
            return game_menu(game_board, building_pool)
        elif choice == 2:
            # code to add random building 2
            return game_menu(game_board, building_pool)
        elif choice == 3:
            # code to see remaining buildings
            return game_menu(game_board, building_pool)
        elif choice == 4:
            # code to see current score
            return game_menu(game_board, building_pool)
        elif choice == 5:
            save_game()
            return game_menu(game_board, building_pool)
        elif choice == 0:
            # code to delete existing game data
            return
        else:
            print("\033[91m{}\033[00m".format("Input options 0-5!"))
            return game_menu(game_board, building_pool)
    except ValueError:
        print("\033[91m{}\033[00m".format("Input options 0-5!"))
        return game_menu(game_board, building_pool)


# Function to save game data


def save_game():
    # getting board data (implement get board function)
    # to change to game data, populating for function testing purpose
    board = {1: "6", 2: "5", 3: "f"}
    pickle_out = open("save.pickle", "wb")
    pickle.dump(board, pickle_out)
    pickle_out.close()


# CREATED FOR UNIT TEST !!!!!!!!!!!!
def save_game(board, pool, file):
    pickle_out = open(file, "wb")
    content = pickle.dump([board, pool], pickle_out)
    pickle_out.close()
    return content

# Function to load game data


def load_game():
    pickle_in = open("save.pickle", "rb")
    board = pickle.load(pickle_in)
    # implement an update function to populate saved board
    # board = city.updatefunction

    # testing whether function works
    print(board)
    return


def main():
    game_board = None
    building_pool = None

    while True:
        print("\nWelcome, mayor of Simp City!")
        print("----------------------------")
        print("\n1. Start new game")
        print("2. Load new game")
        print("\n0. Exit")

        option = input("Your choice? ")

        # Ensure inputted option is valid
        try:
            option = int(option)
            if (option != 1 and option != 2 and option != 0):
                raise ValueError
        except ValueError:
            # print red warning using ANSI escape codes
            print("\033[91m{}\033[00m".format("Invalid option!"))
            continue

        if option == 1:
            if (game_board == None or building_pool == None):
                # Get blank game board and default building pool
                game_board, building_pool = init_game()
            # Start game menu
            game_menu(game_board, building_pool)

        elif option == 2:
            load_game()

        elif option == 0:
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()
