import pygame
import random

class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, cell_pos_x, cell_pos_y, width, height, bomb_chance, font):
        self.x = cell_pos_x * width
        self.y = cell_pos_y * height
        self.pos_x = cell_pos_x
        self.pos_y = cell_pos_y
        self.width = width
        self.height = height
        self.cell_thickness = 2
        self.neighbouring_bombs = 0
        self.selected = False
        self.font = font

        self.cell_center = (
            self.x + self.width // 2,
            self.y + self.width // 2,
        )  # useful for drawing
        self.bomb = (
            random.random() < bomb_chance
        )  # each cell has a chance of being a bomb
        self.color = (0, 64, 0)

    def draw(self, screen):
        """This method is called in the main.py files draw_cells fkn"""
        """Ritar ut enskilda cellerna och senare bomberna och siffrorna"""
        # Hint: Should draw each cell, i.e something to do with pygame.draw.rect
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect, self.cell_thickness)

        if self.selected and not self.bomb:
            text = self.font.render(str(self.neighbouring_bombs), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = self.cell_center
            screen.blit(text, text_rect)

        if self.selected and self.bomb:
            text = self.font.render("X", True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = self.cell_center
            screen.blit(text, text_rect)

        
            
        # Later on in the assignment it will do more as well such as drawing X for bombs or writing digits
        # Important: Remember that pygame starts with (0,0) coordinate in upper left corner!

    
