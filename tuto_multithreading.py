import time
import threading


def process_1():
    for i in range(3):
        print("processing 1")
        time.sleep(0.3)


def process_2():
    for i in range(3):
        print("processing 2")
        time.sleep(0.3)


th1 = threading.Thread(target=process_1)
th2 = threading.Thread(target=process_2)

th1.start()
th2.start()

# all line between start and join will be executed in parallel i.e. without waiting for thread's end
print("PROCESSING 3")

th1.join()
th2.join()

# all line after join will be executed after the threads have finished
