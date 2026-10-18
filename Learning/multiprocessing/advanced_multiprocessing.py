from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square:{number*number}"

numbers= [1,2,3,4,5,6,7,8,9,10]
t1= time.time()

if __name__== "__main__":
#creating multiprocessing 
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    finsished_time= time.time()-t1

    for result in results:
        print(result)