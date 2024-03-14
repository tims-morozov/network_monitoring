import os
import time
from termcolor import colored


hostname = 'gmail.com'
n = 5
counter = 0

while True: 
    try:
        print('|', end='\r', flush=True)
        time.sleep(0.5)
        print('/', end='\r', flush=True)
        time.sleep(0.5)
        print('—', end='\r', flush=True)
        time.sleep(0.5)
        print('\\', end='\r', flush=True)
        time.sleep(0.5)
        print('|', end='\r', flush=True)
        time.sleep(0.5)
        response = os.system("ping -c 1 " + hostname + '>/dev/null 2>&1')
        if response !=0:
            counter += 1
        else:
            counter = 0
        if counter == n:
            print(colored(' Low', 'red'), end='\r', flush=True)
        else:
            print(colored(' Ok ', 'green'), end='\r', flush=True)
        # os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        print('Exiting')
        break



        
    
    
    
