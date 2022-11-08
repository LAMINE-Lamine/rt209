import sys
import threading
import time
def task(i):
    print(f"Task {i} startsf for {i+1}seconde")
    time.sleep(1+1)
    print(f"Task {i} ends")


T = []
for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))
for i in range(len(T)):
    T[i].start()
for i in range(len(T)):
    T[i].join()


if __name__=="__main__":
    sys.exit(task())
