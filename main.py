import pygame
import sys
from pygame.math import Vector2
from snake import SNAKE
from fruit import FRUITS

class MAIN:
    def __init__(self):
        self.cell_number = 15
        self.cell_size = 40
        self.snake = SNAKE(self.cell_size)
        self.fruit = FRUITS(self.cell_number, self.cell_size)
        
        # Initialize pygame font
        self.game_font = pygame.font.Font(None, 50)
    
    def update(self):
        self.snake.move_snake() 
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self, screen):
        self.draw_grass(screen)
        self.snake.draw_snake(screen)
        self.fruit.draw_fruit(screen)
        self.draw_score(screen)

    def draw_grass(self, screen):
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, 
                                               self.cell_size, self.cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, 
                                               self.cell_size, self.cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomise()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_score(self, screen):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))

        apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left, score_rect.centery))

        screen.blit(self.fruit.apple, apple_rect)
        screen.blit(score_surface, score_rect)


def main():
    pygame.init()
    
    cell_number = 15
    cell_size = 40
    
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Snake")
    
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    
    main_game = MAIN()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
        
        screen.fill((175, 215, 70))
        main_game.draw_elements(screen)
        
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()