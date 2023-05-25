"""
In this version of the program, you will implement moving on the map (going north/south/west/east).
Author: Adejumo Toluwani
When: Friday, 24th March, 2023
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


def display_map(grid: list[list[str]], player_position: list[int, int]):
    """
    Displays the map.
    """
    for i in range(len(grid)):  # Iterates over the rows of the grid
        for j in range(len(grid[i])):  # Iterates over the columns of the grid
            if [i, j] == player_position:
                print('@', end='')  # Replaces the character on the player's position with '@'
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


def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    display_map(grid, player_position)
    while True:
        command = get_command()

        if command == 'escape':
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
