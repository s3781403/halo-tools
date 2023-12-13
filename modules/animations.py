import time

loading_chars = ['|', '/', '-', '\\']


def doLoadingAnimation(phrase, num_iter=2):
    for _ in range(num_iter):  # Adjust the number of iterations as needed
        for char in loading_chars:
            print(f"\r{phrase}... {char}", end='')
            time.sleep(0.1)  # Adjust the sleep duration as needed