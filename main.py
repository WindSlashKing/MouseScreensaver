import pyautogui as pg
import random

def main():
    MOUSE_DELAY = 1
    pg.FAILSAFE = False
    current_side = None

    while True:
        goal_x, goal_y = pick_random_coordinates(excluding= current_side)
        pg.moveTo(goal_x, goal_y, MOUSE_DELAY, _pause=False)
        current_x, current_y = pg.position()
        if current_x < 5:
            current_side = "left"
        elif current_x > 1900:
            current_side = "right"
        elif current_y < 5:
            current_side = "top"
        else:
            current_side = "bottom"
            
def pick_random_coordinates(excluding = None) -> tuple:
    """
    Args:
        excluding (int): the wall that should be excluded. left, top, right or bottom
    """

    sides = ["left", "top", "right", "bottom"]
    if excluding:
        sides.remove(excluding)

    picked_side = random.choice(sides)
    # top = 0,0 to 1919,0
    # left = 0,0 to 0,1919
    # right = 1919,0 to 1919, 1079
    # bottom = 0, 1079 to 1919, 1079
    # We will always be picking 1 random number depending on what side we should land on
    if picked_side == "left":
        x = 0
        y = random.randint(0, 1919)
    elif picked_side == "top":
        x = random.randint(0, 1919)
        y = 0
    elif picked_side == "right":
        x = 1919
        y = random.randint(0, 1079)
    else:
        x = random.randint(0, 1919)
        y = 1079

    return (x, y)

if __name__ == "__main__":
    main()