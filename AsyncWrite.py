import threading
import time
class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text=text
        self.out=out
    def run(self):
        f = open(self.out,"a")
        f.write(self.text+"\n")
        f.close()
        time.sleep(5)
        print("Finished Background File Write to "+self.out)
def Main():
    message=input("Enter a string to store:")
    background=AsyncWrite(message,"out.txt")
    background.start()
    print("The program can continue while it writes in another thread")
    print("2 + 2 = ",2+2)
    background.join()
    print("Waited until thread was complete")
    print("2 + 2 = ", 2+2)
if __name__=="__main__":
    Main()
