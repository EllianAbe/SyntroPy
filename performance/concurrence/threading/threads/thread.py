import threading
import time

# Function to count up


def count_up(n):
    for i in range(1, n + 1):
        print(f"Counting up: {i}")
        time.sleep(1)  # Simulate work with a delay

# Function to count down


def count_down(n):
    for i in range(n, 0, -1):
        print(f"Counting down: {i}")
        time.sleep(1)  # Simulate work with a delay


# Main function
if __name__ == "__main__":
    # Number to count up to and down from
    n = 5

    # Create threads for counting up and down
    up_thread = threading.Thread(target=count_up, args=(n,))
    down_thread = threading.Thread(target=count_down, args=(n,))

    # Start the threads
    up_thread.start()
    down_thread.start()

    # Wait for both threads to finish
    up_thread.join()
    down_thread.join()

    print("Both counting up and counting down are done!")
