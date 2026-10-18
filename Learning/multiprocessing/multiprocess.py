import multiprocessing
import time

def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(f"Number:{i}")

def print_letters():
    for i in "ABCDEFGHIJK":
        time.sleep(1)
        print(f"Character:{i}")

#following code is to start execution of program from below
if __name__=="__main__":
    #creating the processes
    process1=multiprocessing.Process(target=print_numbers)
    process2=multiprocessing.Process(target=print_letters)

    #starting the processes
    t1=time.time() #to know current time
    process1.start()
    process2.start()

    # let process to complete
    process1.join()
    process2.join()
    finish_time=time.time()-t1 #to know how much time required
    print(f"Finished Time:{finish_time}")

