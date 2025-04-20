## Multithreading
## When to use Multi Threading
## I/O-bound tasks: Task that spend more time waiting for I/O operations (e.g, file operations, network requests).

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")

##Create 2 thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t=time.time()
t1.start()
t2.start()

## wait for the threads to finish
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)
