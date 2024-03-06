import functools
import time

@functools.cache
def cachenacci(i):
   if i == 1:
     return 1
   if i == 2:
     return 1

   return cachenacci(i-2) + cachenacci(i-1)

def fibonacci(i):
  if i == 1:
    return 1
  if i == 2:
    return 1
    
  return fibonacci(i-2) + fibonacci(i-1)

init = time.time()
for i in range(1, 35):
   print(fibonacci(i))
print('took ', time.time() - init)

init = time.time()
for i in range(1, 40):
   print(cachenacci(i))
print('took ', time.time() - init)

