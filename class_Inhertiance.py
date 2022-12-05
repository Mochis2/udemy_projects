class Animal:

    def __init__(self) -> None:
        self.num_eyes = 2


    def breather(self):
        print('inhale')
    

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.num_eyes = 3  # this will be printed

    def breather(self):
        super().breather()
        print('doing this underwater')

    def swim(self):
        print('im under the water blub help')


        
nemo = Fish()
nemo.swim()
nemo.breather()
print(nemo.num_eyes)