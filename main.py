import pyautogui
import secrets
import sys

from time import sleep

pyautogui.FAILSAFE = False

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
