import multiprocessing
import time


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def compute_factorials_in_processes(numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)
    return results

def main():
    numbers = [150000, 150001, 150002]
    start_time = time.time()
    compute_factorials_in_processes(numbers)
    print("Time taken:", time.time() - start_time)

if __name__ == '__main__':
    main()