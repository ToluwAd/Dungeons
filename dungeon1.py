"""
This program loads a map from a file and finds it's start position.
Author: Adejumo Toluwani
When: Friday, 24th March, 2023.
"""

MAP_FILE = 'cave_map.txt'


def load_map(map_file: str):
    """
    Loads a map from a file as a grid (list of lists)
    """
    with open(map_file, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]  # Remove newline characters and split into a list of strings
    grid = [list(line) for line in lines]  # Split each string into a list of characters

    return grid


def find_start(grid: list[list[str]]):
    """
    Finds the starting position of the player on the map.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return [i, j]

    raise ValueError('Starting position not found on the map!')


def get_command():
    """
    Gets a command from the user.
    """
    user_input = input("Enter a command: ").lower()
    return user_input


def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)  # Load data from a text file into a nested list

    # Display the nested list
    print('Map:')
    for line in grid:
        print(''.join(line))

    # Find and display the starting position
    start_pos = find_start(grid)
    print(f'Start position: {start_pos}')

    # Ask the user for a command
    while True:
        command = get_command()

        # Quits the program if correct command is given.
        if command == 'escape':
            break
        else:
            print('I do not understand.')


if __name__ == '__main__':
    main()
