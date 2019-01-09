import random
"""
Clone of 2048 game.
"""

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0), DOWN: (-1, 0), LEFT: (0, 1), RIGHT: (0, -1)}

def slide(line):
    '''
  Returns the supplied line with all non-zero
  values slid toward the 0th item
  '''
    idx = 0
    result = [0] * len(line)
    for tile in line:
        if tile > 0:
            result[idx] = tile
            idx += 1
    return result


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    tiles = slide(line)
    # replace with your code from the previous mini-project
    for idx, value in enumerate(tiles):
        if value != 0:
            if idx + 1 < len(tiles):
                if value == tiles[idx + 1]:
                    tiles[idx] = 2 * value
                    tiles[idx + 1] = 0
    return slide(tiles)


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0 for col in range(self._grid_width)]
                      for row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
        self._end_positions = {}
        up_end = [(0, col) for col in range(self._grid_width)]
        down_end = [(self._grid_height - 1, col)
                    for col in range(self._grid_width)]
        left_end = [(row, 0) for row in range(self._grid_height)]
        right_end = [(row, self._grid_width - 1)
                     for row in range(self._grid_height)]
        self._end_positions[UP] = [self._grid_height, up_end]
        self._end_positions[DOWN] = [self._grid_height, down_end]
        self._end_positions[LEFT] = [self._grid_width, left_end]
        self._end_positions[RIGHT] = [self._grid_width, right_end]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        message = '\nGrid Size: {height}H x {width}W\n\n'.format(
            height=self._grid_height, width=self._grid_width)
        message += '\t'
        for col_idx in range(self._grid_width):
            message += 'col ' + str(col_idx + 1) + '\t'
        message += '\n'
        for row_idx, row in enumerate(self._grid):
            message += 'row ' + str(row_idx + 1) + '\t'
            for col_idx, col in enumerate(row):
                message += str(col) + '\t'
            message += '\n'
        return message

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        steps = self._end_positions[direction][0]
        end_positions = self._end_positions[direction][1]
        offset = OFFSETS[direction]
        tile_moved = False
        for position in end_positions:
            current_line = []
            for step in range(steps):
                row = position[0] + step * offset[0]
                col = position[1] + step * offset[1]
                current_line.append(self._grid[row][col])
            merged_line = merge(current_line)
            for step in range(steps):
                row = position[0] + step * offset[0]
                col = position[1] + step * offset[1]
                if self._grid[row][col] != merged_line[step]:
                    tile_moved = True
                    self._grid[row][col] = merged_line[step]
        if tile_moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        value = random.choice(([2] * 90) + ([4] * 10))
        row = random.randrange(0, self._grid_height)
        col = random.randrange(0, self._grid_width)
        while self._grid[row][col] != 0:
            row = random.randrange(0, self._grid_height)
            col = random.randrange(0, self._grid_width)
        self._grid[row][col] = value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


if __name__ == '__main__':
    game = TwentyFortyEight(5, 3)
    print(game)
    game.move(UP)
    print(game)
    game.move(UP)
    print(game)
    game.move(LEFT)
    print(game)
    game.move(RIGHT)
    print(game)
    game.move(DOWN)
    print(game)
