from collections import deque
from os import system, name


class Snake:
    def __init__(self):
        self.snakeBody = deque([
            [4, 1],
            [4, 2],
            [4, 3],
            [4, 4],
        ])

    def move(self, direction):
        delta = {
            'up': [-1, 0],
            'do': [1, 0],
            'le': [0, -1],
            'ri': [0, 1],
        }

        currentHead = self.snakeBody[-1]
        currRow, currCol = currentHead
        changeRow, changeCol = delta[direction]
        newHead = [currRow + changeRow, currCol + changeCol]
        self.snakeBody.append(newHead)
        self.snakeBody.popleft()

    def draw(self):
        grid = []
        for i in range(10):
            grid.append([' ' for x in range(10)])

        for pos in self.snakeBody:
            row, col = pos
            # print(row, col, grid)
            grid[row][col] = '0'

        _ = system('clear')
        for row in grid:
            print('|'.join(row))

    def play(self):
        while True:
            keypress = input('Please enter your movement [w|a|s|d]: ')
            if keypress == 'w':
                self.move('up')
            if keypress == 'a':
                self.move('le')
            if keypress == 's':
                self.move('do')
            if keypress == 'd':
                self.move('ri')

            self.draw()


game = Snake()
# game.draw()
# print('-------')
# game.move('up')
# game.draw()
# print('-------')
# game.move('ri')
# game.draw()
game.play()
