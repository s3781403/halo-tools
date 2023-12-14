import time

default_loading_chars = ['|', '/', '-', '\\']


def doLoadingAnimation(phrase, num_iter=2, loading_chars=default_loading_chars, sleep_duration=0.1):
    for _ in range(num_iter):  # Adjust the number of iterations as needed
        for char in loading_chars:
            print(f"\r{phrase}... {char}", end='')
            time.sleep(sleep_duration)  # Adjust the sleep duration as needed