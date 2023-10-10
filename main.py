from classes import Manager
import os
import time


def main():
    manager = Manager()
    while True:
        manager.main_menu()
        time.sleep(1.0)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
