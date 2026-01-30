#thing
import sys
import time as t
def sprint(text, delay=0.035):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
    print() 
sprint("good job mymna")