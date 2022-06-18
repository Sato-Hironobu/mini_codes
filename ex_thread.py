from time import sleep

import threading

def greet(i):
    sleep(i)
    if i != 11 and i % 10 == 1: postfix = "st"
    elif i != 12 and i % 10 == 2: postfix = "nd"
    elif i != 13 and i % 10 == 3: postfix = "rd"
    else: postfix = "th"
    print(f"Hello world from {i}{postfix} thread!")

if __name__ == "__main__":

    for i in range(100):
        hello_handler = threading.Thread(target=greet, args=(i,))
        hello_handler.start()