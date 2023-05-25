"""
In this final program, the map will be displayed to be more visually appeasing and will check if a player wins
Author: Adejumo Toluwani
When: Friday, 24th March, 2023.
"""

MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'


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


def display_map(grid: list[list[str]], player_position: list[int, int]):
    """
    Displays the map.
    """

    # Emojis for displaying the map
    EMOJI_START = '🏠'
    EMOJI_FINISH = '🏺'
    EMOJI_DASH = '🧱'
    EMOJI_PATH = '🟢'
    EMOJI_PLAYER = '🧝'

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if [i, j] == player_position:
                print(EMOJI_PLAYER, end='')
            elif grid[i][j] == 'S':
                print(EMOJI_START, end='')
            elif grid[i][j] == 'F':
                print(EMOJI_FINISH, end='')
            elif grid[i][j] == '-':
                print(EMOJI_DASH, end='')
            elif grid[i][j] == '*':
                print(EMOJI_PATH, end='')
            else:
                print(grid[i][j], end='')
        print()


def get_grid_size(grid: list[list[str]]):
    """
    Gets the size of the grid
    """
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    grid_size = [number_of_rows, number_of_columns]
    return grid_size


def is_inside_grid(grid: list[list[str]], position: list[int, int]):
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)

    # This block of code checks if your position is valid
    if 0 <= position[0] < grid_rows:
        if 0 <= position[1] < grid_cols:
            return True
    else:
        return False


def look_around(grid: list[list[str]], player_position: list[int, int]):
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('east')
    return directions


def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    x, y = player_position
    directions = look_around(grid, player_position)

    if direction == 'north' and 'north' in directions:
        x -= 1
    elif direction == 'south' and 'south' in directions:
        x += 1
    elif direction == 'west' and 'west' in directions:
        y -= 1
    elif direction == 'east' and 'east' in directions:
        y += 1
    else:
        return False

    if is_inside_grid(grid, [x, y]):
        player_position[0] = x
        player_position[1] = y
        return True
    else:
        return False


def check_finish(grid: list[list[str]], player_position: list[int, int]):
    """
    Checks if the player has reached the exit.
    """
    x, y = player_position
    if grid[x][y] == "F":
        return True
    else:
        return False


def display_help():
    """
    Displays a list of commands.
    """
    with open(HELP_FILE, 'r') as file:
        print(file.read())


def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    print("Welcome to the dungeon!")
    print("Find the treasure 'F', avoid the traps '-' and don't fall into the pits 'o'.")
    print("Type 'help' for a list of commands.")
    display_map(grid, player_position)
    while True:
        if check_finish(grid, player_position):
            print("Congratulations! You have reached the exit!")
            break

        command = get_command()
        if command == "help":
            display_help()
        elif command == 'escape':
            print("Goodbye!")
            break
        elif command == 'show map':
            display_map(grid, player_position)
        elif command == 'go north':
            if move('north', player_position, grid):
                print("You moved north.")
            else:
                print("There is no way there.")
        elif command == 'go south':
            if move('south', player_position, grid):
                print("You moved south.")
            else:
                print("There is no way there.")
        elif command == 'go west':
            if move('west', player_position, grid):
                print("You moved west.")
            else:
                print("There is no way there.")
        elif command == 'go east':
            if move('east', player_position, grid):
                print("You moved east.")
            else:
                print("There is no way there.")
        else:
            print("Invalid command")


if __name__ == '__main__':
    main()
