import time

def simple_search(value, numbers):
    for x in numbers:
        if x == value:
            return True 

    return False 

def binary_search(value, numbers):
    low = 0
    high = len(numbers) - 1

    while low <= high:
      
        middle = (low + high) // 2

        if numbers[middle] < value:
            low = middle + 1
        elif numbers[middle] > value:
            high = middle - 1
        else:
            return True

    return False
for length in range(0, 501, 10):
    numbers = list(range(1, length + 1))
    value = length // 2 + 1

    t0 = time.perf_counter_ns()
    simple_search(value, numbers)
    t1 = time.perf_counter_ns()
    binary_search(value, numbers)
    t2 = time.perf_counter_ns()

    simple_runtime = t1 - t0
    binary_runtime = t2 - t1
    print(length, simple_runtime, binary_runtime, sep=';')
    