import os, time, tkinter as tk
from termcolor import colored
from playsound import playsound


default_hostname = 'gmail.com'
default_delay = 5
        
def propeller(delay):
    blades = ['|', '/', '—', '\\']
    stop = time.time() + delay

    while stop > time.time():
        for i in blades:
            Entry_Propeller.delete(0, tk.END)
            Entry_Propeller.insert(0, i)
            Entry_Propeller.update()
            time.sleep(0.5)

def hide_elements():
    Label_Hostname.grid_remove()
    Label_Delay.grid_remove()
    Entry_Hostname.grid_remove()
    Entry_Delay.grid_remove()
    Run_button.grid_remove()
    window.geometry('430x30')

def run_ping():
    hostname = Entry_Hostname.get()
    delay = Entry_Delay.get()
    delay = int(delay)

    hide_elements()

    while True: 
        response = os.system("ping -c 1 " + hostname + '>/dev/null 2>&1')

        if response !=0: 
            playsound('/home/tims/Desktop/Python/Projects/Network_Monitoring/error_message.mp3', block=False)
            Entry_Output.config(foreground='red')
            Entry_Output.delete(0, tk.END)
            Entry_Output.insert(0, "Low")
            Entry_Output.update()

            print(colored(' Low\a', 'red'), end='\r', flush=True)
        else:
            Entry_Output.config(foreground='green')
            Entry_Output.delete(0, tk.END)
            Entry_Output.insert(0, "Ok")
            Entry_Output.update()

            print(colored(' Ok ', 'green'), end='\r', flush=True)

        propeller(delay)


window = tk.Tk()
window.title("Network Monitoring")
window.geometry('540x130')  

Label_Hostname = tk.Label(window, text="Hostname: ")
Label_Hostname.grid(row=0, pady=2, sticky=tk.W)

Label_Delay = tk.Label(window, text="Delay: ")
Label_Delay.grid(row=1, pady=3, sticky=tk.W)

Entry_Hostname = tk.Entry(window, width=20)
Entry_Hostname.grid(row=0, column=1, sticky=tk.EW)
Entry_Hostname.insert(0, default_hostname)

Entry_Delay = tk.Entry(window, width=5)
Entry_Delay.grid(row=1, column=1, sticky=tk.EW)
Entry_Delay.insert(0, default_delay)

Entry_Output = tk.Entry(window, width=35, foreground='gray')
Entry_Output.grid(row=2, column=1, sticky=tk.EW)
Entry_Output.insert(0, "Output")

Entry_Propeller = tk.Entry(window, width=3)
Entry_Propeller.grid(row=2, column=3)

Run_button = tk.Button(window, text="Run", command=run_ping)
Run_button.grid(row=3, column=1, sticky=tk.EW)


window.mainloop()
