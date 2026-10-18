from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):

        time.sleep(2)
        return f"Number:{numbers}"

nums=[1,2 ,3,4,5,6,7]

t1= time.time()

#creating 5 threads
with ThreadPoolExecutor(max_workers=5) as executor:
        results=executor.map(print_numbers, nums)

finish_time=time.time()-t1
for result in results:
        print(result)

print(f"Finished Time: {finish_time}")