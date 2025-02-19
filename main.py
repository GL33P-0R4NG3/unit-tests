import logging
import random

logging.basicConfig(
    level=logging.DEBUG,
    filename="../Temp/log",
    format="[%(asctime)s.%(msecs)03d] %(levelname)-7s| %(process)06d >> %(thread)d | %(filename)s:%(lineno)d %(funcName)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

def main():
    # TODO: we need to make more messages
    MESSAGES = [
        "I can read your mind",
        "I can buy you flowers",
        "I can shower with you",
        "I can take you hiking",
        "I can send you letter",
        "I can use toilet",
        "I can bake you cake"
    ]

    print("Working...")

    logging.info("Script started...")
    logging.debug("I do many things >:D!")

    i = 0

    while True:
        a = random.randint(0, 314)
        if a % 6 == 0:
            logging.debug("They are calling... See you later!")
            break
        if a % 2 == 0:
            logging.debug(MESSAGES[random.randint(0, len(MESSAGES) - 1)])
        if i == 10:
            logging.warning("Wow we hit %d. Such a big number", i)
        if a % 10 == 0:
            logging.error("Exceeded precise calculation your results might not be accurate!")
        i += 1

    logging.info("Script Ended")

    print("Log Saved!")

if __name__ == "__main__":
    main()