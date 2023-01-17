class Car:
    def __init__(self,model,year=2023):
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self):
        print('Vroom')
        self.miles_driven +=1

    def info(self):
        print(f'Number of miles driven :{self.miles_driven}')
        print(f'Model name: {self.model}')
        print(f'Year: {self.year}')

car1=Car('Tesla')
print(car1.drive())
print(car1.info())