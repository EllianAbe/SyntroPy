**Multiprocessing Pool Example**
=====================================

This script demonstrates the use of the `multiprocessing` module in Python to parallelize a task using a pool of worker processes.

**Overview**
------------

The script defines a simple task function `task(n)` that simulates some work by sleeping for 5 seconds and then returns the square of the input number `n`. The `main()` function creates a pool of 10 worker processes and uses the `pool.map()` function to apply the `task()` function to a range of numbers from 1 to 101.

**Usage**
---------

To run the script, simply execute the `pool.py` file using Python:
```bash
python pool.py
```
This will start the pool of worker processes and execute the task function in parallel. The results will be printed to the console.

**Code Structure**
-----------------

The script consists of three main functions:

* `task(n)`: the task function that simulates some work and returns the square of the input number `n`.
* `main()`: the main function that creates the pool of worker processes and applies the `task()` function to a range of numbers.
* `if __name__ == "__main__":`: the guard clause that ensures the `main()` function is only executed when the script is run directly (i.e., not when it is imported as a module by another script).

**Notes**
-------

* The `multiprocessing` module is used to create a pool of worker processes that can execute tasks in parallel.
* The `pool.map()` function is used to apply the `task()` function to a range of numbers in parallel.
* The `if __name__ == "__main__":` guard clause is used to ensure that the `main()` function is only executed when the script is run directly.