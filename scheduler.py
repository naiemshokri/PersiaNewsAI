import time


def wait_next_cycle(minutes=5):

    seconds = minutes * 60

    print()
    print(f"Sleeping {minutes} minutes...")
    print()

    time.sleep(seconds)
