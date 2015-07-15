import time

from bot import HuggyBot


INTERVAL = 1.0


def main():
    huggy_bot = HuggyBot()
    while True:
        huggy_bot.process_updates()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
