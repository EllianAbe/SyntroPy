import concurrent.futures
import time


def task(n):
    time.sleep(5)  # Simulate some work
    print(f"Task {n} finished")
    return n * n


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(1, 101):
            futures.append(executor.submit(task, i))

        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    print("Results:", results)


if __name__ == "__main__":
    main()
