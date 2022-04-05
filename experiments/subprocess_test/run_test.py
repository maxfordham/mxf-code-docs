from io import StringIO
import os
import subprocess
import sys

def show1():
    print( 'start show1')
    save = sys.stdout
    sys.stdout = StringIO()
    print( 'sys.stdout being buffered')
    proc = subprocess.Popen(['echo', 'hello'])
    print(type(proc))
    proc.wait()
    in_stdout = sys.stdout.getvalue()
    sys.stdout = save
    print ('in buffer:', in_stdout)
    
def show1_1():
    print( 'start show1_1')
    save = sys.stdout
    sys.stdout = StringIO()
    print( 'sys.stdout being buffered')
    proc = subprocess.run(['echo', 'hello'])
    proc.wait()
    in_stdout = sys.stdout.getvalue()
    sys.stdout = save
    print ('in buffer:', in_stdout)

def show2():
    print ('start show2')
    save = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    print ('after redirect sys.stdout')
    proc = subprocess.Popen(['echo', 'hello'])
    proc.wait()
    sys.stdout = save

show1()
#show1_1()
show2()