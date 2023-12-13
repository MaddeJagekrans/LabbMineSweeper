import pygame
import sys
from cell import Cell

""" This is the main file you work on for the project"""

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.25  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells  # how large can each cell be?
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, CELL_SIZE)

pygame.display.set_caption("MineSweeper")


cells = []
#board = []

def create_cells():
    """This function is meant to initially generate all the cells and create the boundaries"""
    width = CELL_SIZE
    height = CELL_SIZE
    
    for cell_y in range(amount_of_cells):
        cells.append([])

        for cell_x in range(amount_of_cells):
            cell = Cell(cell_x, cell_y, width, height, bomb_chance, font)

            cells[cell_y].append(cell)
   
    # This is a good base to go from (think about it thoroughly before you code!! We want to create 16x16 list with each object being a cell):
    #for a_row in range(amount_of_cells):
     #   row = []
      #  for a_column in range(amount_of_cells):
       #     pass

    pass


def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    for col in cells:
        for cell in col:
            cell.draw(screen)


def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    screen.fill((0, 0, 0))
    draw_cells()


def calc_cell_pos(position):
    """This function calculates the cell position of the mouse"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    center_x = position[0] // CELL_SIZE
    center_y = position[1] // CELL_SIZE

    return (center_x, center_y)


def event_handler(event):
    """This function handles all events in the program"""
    if event.type == pygame.QUIT:
        terminate_program()
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        cell_grid_pos_x, cell_grid_pos_y = calc_cell_pos(pygame.mouse.get_pos())
        cell = cells[cell_grid_pos_y][cell_grid_pos_x]
        if cell.bomb:
            terminate_program()
            
        cell.on_click()




def run_setup():
    """This function is meant to run all code that is neccesary to setup the app, happends only once"""
    create_cells()


def terminate_program():
    """Functionality to call on whenever you want to terminate the program"""
    pygame.quit()
    sys.exit()


def main():
    run_setup()

    while True:
        for event in pygame.event.get():
            event_handler(event)

        draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
