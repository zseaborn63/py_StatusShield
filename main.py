import pyautogui
import secrets
import sys

from time import sleep

pyautogui.FAILSAFE = False


def choose_random_number(inclusive_min, exclusive_max):
    """
        Utility function designed to choose a random number between two given numbers.  The lower-bound number will be
        included in the selection pool but the upper-bound number will be excluded from selection. Utilize the secrets
        module to be more secure.

    :param int inclusive_min: The minimum number that can be returned by this function.
    :param int exclusive_max: The maximum number + 1 that can be returned by this function.
    :return: random integer between the given inclusive_min and exclusive_max arguments.
    :rtype: integer
    """
    num = 0
    while num < inclusive_min:
        num = secrets.randbelow(exclusive_max)

    return num



def move_mouse_randomly():
    """
        Move the mouse pointer 4-9 times to a randomly chosen set of coordinates on the screen.  It will be randomly
        chosen to take between 1 and 5 seconds for the shift in mouse pointer position to occur.  The program will sleep
        for 6-10 seconds, chosen at random each time, in between pointer shifts.

    :return: N/A
    """

    max_wiggles = choose_random_number(4, 10)

    screen = pyautogui.size()
    width_max = screen[0] - 200
    height_max = screen[1] - 200

    for _ in range(1, max_wiggles):
        print("Shifting Shield!")
        _rand_x = choose_random_number(100, width_max)
        _rand_y = choose_random_number(100, height_max)
        _rand_duration = choose_random_number(1, 6)
        pyautogui.moveTo(
            x=_rand_x,
            y=_rand_y,
            duration=_rand_duration
        )
        sleep_num = choose_random_number(6, 11)
        sleep(sleep_num)


def perform_cycle():
    """"""
    return


if __name__ == '__main__':
    print("Raising the StatusShield ...")
    print("Press 'Ctrl' + 'C' to lower the StatusShield.")
    try:
        while True:
            perform_cycle()
    except KeyboardInterrupt:
        print("Stowing the StatusShield away.")
