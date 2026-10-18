import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letters():
    for i in "lmnopqr":
        time.sleep(2)
        print(f"Character:{i}")

#creating threads 
thread1= threading.Thread(target=print_numbers)
thread2= threading.Thread(target=print_letters)

t=time.time()

#following code starts the threads
thread1.start()
thread2.start()

#following code waits for the thread to complete
thread1.join()
thread2.join()

finished_time=time.time()-t
print(f"Finished Time:{finished_time}")
