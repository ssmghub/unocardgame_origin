# from menus.main import main
from menu import StartMenu
import Board
from menu import WinEndMenu
from menu import LoseEndMenu

if(__name__ == '__main__'):
    menu_label = "" #to mark the menu 
    # rectangles ={} # to mark the existing Rect's

    StartMenu.startMenu(menu_label)
    # Board.board("PlayBoard")
    # WinEndMenu.winEndMenu("Win",1,2,3,4)
    # LoseEndMenu.loseEndMenu("Lose",1,2,3,4)


