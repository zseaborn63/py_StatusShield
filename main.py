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
