import pygame
import sys
from cell import Cell
from calcs import measure_distance

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

pygame.display.set_caption("MineSweeper")

font = pygame.font.Font(None, CELL_SIZE)
text_surface = font.render('8', True, (255, 255, 255))
text_rect = text_surface.get_rect()

rendered_chars = []
cells = []


def create_cells():
    """This function is meant to initially generate all the cells and create the boundaries"""
    x = 0
    y = 0
    width = CELL_SIZE
    height = CELL_SIZE
    
    for _column in range(amount_of_cells):
        for _row in range(amount_of_cells):
            cell = Cell(x,y,width,height,bomb_chance)
            cells.append(cell)
            x += width

        y += height
        x = 0
   
    # This is a good base to go from (think about it thoroughly before you code!! We want to create 16x16 list with each object being a cell):
    #for a_row in range(amount_of_cells):
     #   row = []
      #  for a_column in range(amount_of_cells):
       #     pass

    pass


def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    for cell in cells:
         cell.draw(screen)


def draw_bombs():
    pass


def draw_character_in_cell():
    """Draws a number in a cell"""
    # få mitten av cellen : 
    
    for text_surface, text_rect in rendered_chars:
        #cell_center_x = cells[0] + CELL_SIZE // 2
        #cell_center_y = cells[1] + CELL_SIZE // 2
        #cell_center = cell_center_x + cell_center_y
        screen.blit(text_surface, text_rect)



def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    screen.fill((0, 0, 0))
    draw_cells()
    draw_character_in_cell()
    
   


def cacl_cell_pos(mouse_pos):
    """This function calculates the cell position of the mouse"""
    x = mouse_pos[0] // CELL_SIZE
    y = mouse_pos[1] // CELL_SIZE 
    draw_character_in_cell(cells[x,y])
    
    #return cells[x,y]

    pass


def event_handler(event):
    """This function handles all events in the program"""
    if event.type == pygame.QUIT:
        terminate_program()
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        clicked_x, clicked_y = pygame.mouse.get_pos()
        text_rect.centerx = clicked_x
        text_rect.centery = clicked_y

        rendered_chars.append((text_surface, text_rect.copy()))

        print(clicked_x, clicked_y)
        #cacl_cell_pos(mouse_pos)
        #draw_cells(mouse_pos)


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

    terminate_program()


if __name__ == "__main__":
    main()
