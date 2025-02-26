import pyautogui
import secrets
import sys

from datetime import datetime
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


def print_msg(msg):
    """
        Quick way to print a message preceded by the datetime of its printing.

    :param str msg: Message to be printed with the datetime
    :return: N/A
    """
    _now = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]
    print(f"{_now}:  {msg}")


def change_active_window():
    """
        Switch the active window 1-5 times in quick succession, sleeping for a very short duration, which is also chosen
            at random, in between the window changes.

    :return: N/A
    """
    print_msg("Repainting Shield!")

    sleep_times = [float(f"0.{choose_random_number(11, 16)}") for _ in range(1, choose_random_number(1, 6))]

    pyautogui.keyDown('alt')

    for _sleep_time in sleep_times:
        pyautogui.press('tab')
        sleep(_sleep_time)  # Issues:  "How to introduce randomness here": "how to make it a float?": "how to make it a list comprehension?"

    pyautogui.keyUp('alt')


def move_mouse_randomly():
    """
        Move the mouse pointer 4-9 times to a randomly chosen set of coordinates on the screen.  It will be randomly
            chosen to take between 1 and 5 seconds for the shift in mouse pointer position to occur.  The program will
            sleep for 6-10 seconds, chosen at random each time, in between pointer shifts.

    :return: N/A
    """

    # Get the current screen params and set our boundaries
    screen = pyautogui.size()
    width_max = screen[0] - 200
    height_max = screen[1] - 200
    coordinates_min = 100

    # Choose a random number of reposition coordinates, which are themselves randomly chosen based on the screen params
    repositions = [
        (
            choose_random_number(coordinates_min, width_max),
            choose_random_number(coordinates_min, height_max),
        ) for _ in range(1, choose_random_number(4, 10))
    ]

    for coordinates in repositions:
        print_msg("Shifting Shield!")

        _rand_duration = choose_random_number(1, 6)
        pyautogui.moveTo(
            x=coordinates[0],
            y=coordinates[1],
            duration=_rand_duration
        )

        sleep_num = choose_random_number(6, 11)
        sleep(sleep_num)


def perform_cycle():
    """
        Perform one 'cycle' of the StatusShield.  This involves changing the active window, moving the mouse at random,
            force-clearing stdout, and sleeping for a random period of time between 20 and 60 seconds.

    :return: N/A
    """
    print_msg("Shielding the Status!!")

    change_active_window()
    move_mouse_randomly()
    sys.stdout.flush()

    sleep_time = choose_random_number(20, 61)
    print_msg(f"Resting for just a moment, only {sleep_time} seconds, and then back to work!")
    sleep(sleep_time)


if __name__ == '__main__':
    print_msg("Raising the StatusShield ...")
    print_msg("Press 'Ctrl' + 'C' to lower the StatusShield.")
    try:
        while True:
            perform_cycle()
    except KeyboardInterrupt:
        print_msg("Stowing the StatusShield away.")
