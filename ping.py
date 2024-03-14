import os
import argparse
import time
from termcolor import colored


parser = argparse.ArgumentParser(description='Parse of hostname and max_attempts')
parser.add_argument("h")
parser.add_argument("-a")
args = parser.parse_args()

hostname = args.h 
max_attempts = args.a

counter = 0

def propeller():
    blades = ['|', '/', '—', '\\']
    for _ in range(2):
        for i in blades:
            print(i, end='\r', flush=True)
            time.sleep(0.5)
        
while True: 
    try:
        propeller()
        
        response = os.system("ping -c 1 " + hostname + '>/dev/null 2>&1')
        if response !=0:
            counter += 1
        else:
            counter = 0
        if counter == max_attempts:
            print(colored(' Low', 'red'), end='\r', flush=True)
        else:
            print(colored(' Ok ', 'green'), end='\r', flush=True)
        # os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        print('Exiting')
        break



        
    
    
    
