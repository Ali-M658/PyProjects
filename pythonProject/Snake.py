import tkinter as tk
import random


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.width = 400
        self.height = 400
        self.cell_size = 20

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()

        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = 'Right'
        self.food_position = self.place_food()
        self.score = 0

        self.root.bind('<Key>', self.change_direction)
        self.game_over = False

        self.run_game()

    def place_food(self):
        x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
        y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
        return (x, y)

    def change_direction(self, event):
        if event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def run_game(self):
        if not self.game_over:
            self.update_snake()
            self.check_collisions()
            self.draw_elements()
            self.root.after(100, self.run_game)

    def update_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'Up':
            head_y -= self.cell_size
        elif self.direction == 'Down':
            head_y += self.cell_size
        elif self.direction == 'Left':
            head_x -= self.cell_size
        elif self.direction == 'Right':
            head_x += self.cell_size

        new_head = (head_x, head_y)

        if new_head == self.food_position:
            self.score += 1
            self.food_position = self.place_food()
        else:
            self.snake.pop()  # Remove the tail if not eating food

        self.snake.insert(0, new_head)  # Add new head

    def check_collisions(self):
        head_x, head_y = self.snake[0]

        # Check wall collisions
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            self.game_over = True

        # Check self collisions
        if len(self.snake) > 1 and self.snake[0] in self.snake[1:]:
            self.game_over = True

    def draw_elements(self):
        self.canvas.delete(tk.ALL)

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='green')

        # Draw food
        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + self.cell_size, food_y + self.cell_size, fill='red')

        # Game over text
        if self.game_over:
            self.canvas.create_text(self.width // 2, self.height // 2, text="Game Over!", fill="white",
                                    font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
