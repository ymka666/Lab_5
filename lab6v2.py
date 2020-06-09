# 7 - Визначити ієрархію рухомого складу залізничного транспорту. Створити пасажирський потяг.
# Порахувати загальну чисельність пасажирів і багажу в потязі. Провести сортування вагонів потягу за рівнем комфортності.
# Знайти вагон в потязі, що відповідає заданому діапазону кількості пасажирів.

import random as r

class Rail_Transport:

    def __init__(self, name):
        self.name = name

class Car_Head(Rail_Transport):

    def __init__(self, name):
        super().__init__(name)

    def gen_head(self):
        return {'train':self.name, 'type':'head', 'passengers':r.randint(3,5), 'baggage':r.randint(5,15), 'comfort':r.randint(0,10)}


class Car_Plackart(Rail_Transport):
    
    def __init__(self, name):
        super().__init__(name)

    def gen_plackart(self):
        return {'train':self.name, 'type':'plackart', 'passengers':r.randint(30,60), 'baggage':r.randint(40,100), 'comfort':r.randint(0,10)}


class Car_Kupe(Rail_Transport):

    def __init__(self, name):
        super().__init__(name)

    def gen_kupe(self):
        return {'train':self.name, 'type':'kupe', 'passengers':r.randint(30,60), 'baggage':r.randint(30,80), 'comfort':r.randint(4,10)}


class Car_Luxury(Rail_Transport):

    def __init__(self, name):
        super().__init__(name)

    def gen_luxury(self):
        return {'train':self.name, 'type':'luxury', 'passengers':r.randint(20,40), 'baggage':r.randint(20,60), 'comfort':r.randint(6,10)}




class Train:

    letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','G','H','J','K','L','Z','X','C','V','B','N','M']

    def __init__(self):
        self.name = self.gen_name()
        self.body = self.gen_train()

    def __repr__(self):
        info = ""
        for i in range(1, len(self.body)+1):
            info += "\nTrain {name}\nCar №{num}: type - {type}, passengers - {passengers} people, baggage - {baggage} kg., comfort - {comfort}/10.\n".format(name=self.body[i]['train'], num=i, type=self.body[i]['type'], passengers=self.body[i]['passengers'], baggage=self.body[i]['baggage'], comfort=self.body[i]['comfort'])
        return info

    def gen_name(self):
        """Генерування ім'я потягу"""
        #Генерую ім'я виду АА-123
        name = ""
        for i in range(2): name += r.choice(self.letters)
        name += "-" + str(r.randint(100,1000))
        return name

    def gen_train(self):
        """Генерує потяг"""
        total = r.randint(10,20)
        train = {i:None for i in range(1, total+1)}
        train[1] = Car_Head(name=self.name).gen_head()
        types = ['plackart', 'kupe', 'luxury']
        for i in range(2, total+1):
            choice = r.choice(types)
            if choice == 'plackart':
                train[i] = Car_Plackart(name=self.name).gen_plackart()
            elif choice == 'kupe':
                train[i] = Car_Kupe(name=self.name).gen_kupe()
            elif choice == 'luxury':
                train[i] = Car_Luxury(name=self.name).gen_luxury()   
        return train

    def total_passengers(self):
        """Рахує загальку кількість пасажирів в потязі"""
        count = 0
        for i in range(1, len(self.body)+1):
            count += self.body[i]['passengers']
        print(f"Train {self.name}: total passengers - {count} people.\n")

    def total_baggage(self):
        """Рахує загальну кількість багажу в потязі"""
        count = 0
        for i in range(1, len(self.body)+1):
            count += self.body[i]['baggage']
        print(f"Train {self.name}: total baggage - {count}kg.\n")

    def sort_by_comfort(self):
        """Сортує вагони потягу за степенем комфорту по спаданню"""
        train_sorted = sorted(self.body.items(), key=lambda x: x[1]['comfort'], reverse=True)
        print(f"\nTrain {self.name}, sorted by comfort:\n")
        for i in train_sorted:
            print(f"Car №{i[0]}: comfort {i[1]['comfort']}/10.")

    def find_car_by_passengers(self, start, end):
        """Пошук вагонів, в яких кількість пасажирів задовільняє заданий діапазон"""
        amount = 0
        print(f"\nTrain {self.name} - suitable cars for your request:\n")
        for i in range(1, len(self.body)+1):
            if start <= self.body[i]['passengers'] <= end:
                print(f"Car №{i}: passengers - {self.body[i]['passengers']} people.")
                amount+=1
        if amount == 0: print("There is no car with the number of passengers that is in your range.")



if __name__ == '__main__':
    train_1 = Train()
    print(train_1)
    print("-"*15)
    print("Enter the range of passengers to find cars.")
    while 1:
        start = input("Enter start: ")
        try:
            start = int(start)
            break
        except ValueError:
            print("Incorrect input, try again.")
    while 1:
        end = input("Enter end: ")
        try:
            end = int(end)
            break
        except ValueError:
            print("Incorrect input, try again.")
    if start > end: start, end = end, start
    print("-"*15)
    train_1.total_passengers()
    train_1.total_baggage()
    print("-"*15)
    train_1.sort_by_comfort()
    print("-"*15)
    train_1.find_car_by_passengers(start=start, end=end)
