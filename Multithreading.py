import threading
import time
tLock=threading.Lock()
def timer(name,delay,repeat):
    print("Timer: "+name+" Started")
    tLock.acquire() # Only locked thread will continue
                    # Another threads are just waiting
    print(name+" has acquired the lock")
    while repeat>0:
        time.sleep(delay)
        print(name+ ": "+str(time.ctime(time.time())))
        repeat-=1
    print(name+" is realeasing the lock")
    tLock.release() # Don't forget to release lock
    # If it isn't done, then another threads are waiting eternally
    print("Timer: "+name+" Completed")
def Main():
    t1 = threading.Thread(target=timer, args=("Timer1",1,5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main Completed")
if __name__=="__main__":
    Main()
