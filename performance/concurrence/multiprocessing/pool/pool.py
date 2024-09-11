import multiprocessing
import time


def task(n):
    time.sleep(5)  # Simulate some work
    print(f"Task {n} finished")
    return n * n


def main():
    with multiprocessing.Pool(processes=10) as pool:
        results = pool.map(task, range(1, 101))

    print("Results:", results)


if __name__ == "__main__":
    main()
