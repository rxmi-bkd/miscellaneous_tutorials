import tracemalloc

# note that trace malloc will slow down your program
# so use it only for debugging


def foo():
    ...


tracemalloc.start()

foo()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

tracemalloc.stop()
