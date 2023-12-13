import pygame
import random

class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, cell_pos_x, cell_pos_y, width, height, bomb_chance, font):
        self.x = cell_pos_x * width
        self.y = cell_pos_y * height
        self.width = width
        self.height = height
        self.cell_thickness = 2
        self.neighbouring_bombs = 7
        self.selected = False
        self.font = font

        self.cell_center = (
            self.x + self.width // 2,
            self.y + self.width // 2,
        )  # useful for drawing
        self.bomb = (
            random.random() < bomb_chance
        )  # each cell has a chance of being a bomb

        # for debugging, draw gray outline for bomb cells
        if self.bomb:
            self.color = (128, 128, 128)  # RGB color
        else:
            self.color = (0, 64, 0)

    def draw(self, screen):
        """This method is called in the main.py files draw_cells fkn"""
        """Ritar ut enskilda cellerna och senare bomberna och siffrorna"""
        # Hint: Should draw each cell, i.e something to do with pygame.draw.rect
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect, self.cell_thickness)

        if self.selected:
            # draw number in font
            text = self.font.render(str(self.neighbouring_bombs), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = self.cell_center
            screen.blit(text, text_rect)
        # Later on in the assignment it will do more as well such as drawing X for bombs or writing digits
        # Important: Remember that pygame starts with (0,0) coordinate in upper left corner!

    def on_click(self):
        self.selected = True


    def update(self):
        pass

    def get_cell_center(self):
        """This method is called in the main.py files calc_cell_pos fkn"""
        """Returnerar cellens center"""
        return self.cell_center
    
