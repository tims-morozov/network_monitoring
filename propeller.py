import time

class Propeller:
    def __init__(self, delay):
        self.blades = ['|', '/', '—', '\\']
        self.delay = delay

    def run(self):
        stop = time.time() + self.delay
        while stop > time.time():
            for i in self.blades:
                print(i, end='\r', flush=True)
                time.sleep(0.5)

propeller = Propeller(5)
propeller.run()

# def propeller():
#     blades = ['|', '/', '—', '\\']
#     for _ in range(2):
#         for i in blades:
#             print(i, end='\r', flush=True)
#             time.sleep(0.5)
