import asyncio

# Asynchronous function to count up to a number


async def count_up(n):
    for i in range(1, n + 1):
        print(f"Counting up: {i}")
        await asyncio.sleep(1)  # Simulate work with a delay

# Asynchronous function to count down from a number


async def count_down(n):
    for i in range(n, 0, -1):
        print(f"Counting down: {i}")
        await asyncio.sleep(1)  # Simulate work with a delay

# Main function


async def main():
    n = 5

    # Create tasks
    up_task = asyncio.create_task(count_up(n))
    down_task = asyncio.create_task(count_down(n))

    # Wait for both tasks to complete
    await up_task
    await down_task

    print("Both counting up and counting down are done!")

# Run the event loop
asyncio.run(main())
