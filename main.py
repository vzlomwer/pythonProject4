import random

class Student:
    def __init__(self, name,):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive =True
        self.alive = True
        self.money = 0



    def to_study(self):
        print('Time to study...')
        self.progress +=0.2
        self.gladness -=6


    def to_sleep(self):
        print('Time to sleep...')
        self.gladness +=5


    def to_chill(self):
        print('Time clill...')
        self.progress -= 0.1
        self.gladness += 20
        self.money -= 20


    def to_work(self):
        print('Time work...')
        self.progress += 0.4
        self.gladness -=0.1
        self.money += 40


    def is_alive(self):
        if self.progress <= -0.5:
            print ('Cast out...')
        elif self.gladness <=0:
            print ('Depression')
        elif self.money <=0:
            print ('Bankrut')



    def live(self, day):
        print(f"{day:-^50}")
        mon_mon = self.money
        sl_sl = self.gladness
        prod_r = self.progress
        if mon_mon < 30:
            self.to_work()
            print(f'money {self.money}')
            print(f'gladness {self.gladness}')
            print(f'progress {self.progress}')
        elif sl_sl < 4:
            self.to_chill
            print(f'money {self.money}')
            print(f'gladness {self.gladness}')
            print(f'progress {self.progress}')
        elif sl_sl < 2:
            self.to_sleep
            print(f'money {self.money}')
            print(f'gladness {self.gladness}')
            print(f'progress {self.progress}')
        elif prod_r < 3:
            self.to_study()
            print(f'money {self.money}')
            print(f'gladness {sl_sl}')
            print(f'progress {self.progress}')







nick = Student(name='nick')
for day in range(1, 365):
    if nick.live(day) == False:
        break
    nick.live(day)


