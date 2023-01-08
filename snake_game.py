from typing import Optional
from game_display import GameDisplay

class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
        elif (self.__key_clicked == 'Right') and (self.__x < 40):
            self.__x += 1

    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        pass
    
    def is_over(self) -> bool:
    #if snake head goes out of bounds game ends
    if self.__x >= game_utils.WIDTH or self.__x < 0:
        return True
    if self.__y >= game_utils.HEIGHT or self.__y <=0:
        return True
    #if snake head bumps into itself game ends
    for block in self.cells[0:len(self.cells)-2]:
        if self.__x  == block[0] and self.__y == block[1]:
            return True
    return False

