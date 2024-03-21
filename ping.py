import os, argparse
from termcolor import colored
from propeller import Propeller


parser = argparse.ArgumentParser(description='The program pings the server to check the Internet connection')
parser.add_argument("h")
parser.add_argument("-a")
args = parser.parse_args()

hostname = args.h
max_attempts = int(args.a)

counter = 0

        
while True: 
    try:
        propeller = Propeller(5)
        propeller.run()

        response = os.system("ping -c 1 " + hostname + '>/dev/null 2>&1')
        if response !=0:
            counter += 1
        else:
            counter = 0
        if counter >= max_attempts:
            print(colored(' Low', 'red'), end='\r', flush=True)
        else:
            print(colored(' Ok ', 'green'), end='\r', flush=True)
        # os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        print('Exiting')
        break



        
    
    
    
