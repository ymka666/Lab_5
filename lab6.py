# 7 - Визначити ієрархію рухомого складу залізничного транспорту. Створити пасажирський потяг.
# Порахувати загальну чисельність пасажирів і багажу в потязі. Провести сортування вагонів потягу за рівнем комфортності.
# Знайти вагон в потязі, що відповідає заданому діапазону кількості пасажирів.

import random as r

class Rail_Transport:

	def __init__(self, name, cars):
		self.name = name
		self.cars = cars


class Passengers(Rail_Transport):

	def __init__(self, name, cars):
		super().__init__(name, cars)
		#Рахую кількість всіх пасажирів
		self.total_passengers = 0
		for car in self.cars:
			self.total_passengers += self.cars[car]['passengers']

	def __str__(self):
		return "\n\nTrain {name}: total passengers - {total} people.\n\n".format(name=self.name, total=self.total_passengers)



class Baggage(Rail_Transport):

	def __init__(self, name, cars):
		super().__init__(name, cars)
		#Рахую кількість всього багажу
		self.total_baggage = 0
		for car in self.cars:
			self.total_baggage += self.cars[car]['baggage']

	def __str__(self):
		return "\n\nTrain {name}: total baggage - {total} kg.\n\n".format(name=self.name, total=self.total_baggage)


class Comfort_of_Cars(Rail_Transport):

	def __init__(self, name, cars):
		super().__init__(name, cars)
		#Сортую вагони за степенем комфорту по спаданню
		self.sort_cars = sorted(self.cars.items(), key=lambda x: x[1]['comfort'], reverse=True)

	def __str__(self):
		info = "\n\nTrain {name}, sorting by comfort:\n\n".format(name=self.name)
		for car in self.sort_cars:
			info += "Car {number}: comfort - {comfort}/10.\n".format(number=car[0], comfort=car[1]['comfort'])
		return info


class Train:

	letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','G','H','J','K','L','Z','X','C','V','B','N','M']

	def __init__(self):
		self.name = self.gen_name()
		self.cars = self.generation_cars()


	def __repr__(self):
		"""Виведення потягу, який створився"""
		info = "\nTrain {name}:\n".format(name=self.name)
		for car in self.cars:
			info+= "	Car №{number}:  passengers: {passengers} people, baggage: {baggage} kg., comfort: {comfort}/10\n".format(number=car, passengers=self.cars[car]['passengers'], baggage=self.cars[car]['baggage'], comfort=self.cars[car]['comfort'])
		return info


	def gen_name(self):
		"""Генерування ім'я потягу"""
		#Генерую ім'я виду АА-123
		name = ""
		for i in range(2): name += r.choice(self.letters)
		name += "-" + str(r.randint(100,1000))
		return name


	def generation_cars(self):
		"""Генерування потягу"""
		#Генерую потяг. В мене це словник виду {номер вагону:{пасажири:кількість, багаж:кількість, комфорт:степінь}...}
		cars_total = r.randint(10,20)
		return {car:{'passengers':r.randint(30,60), 'baggage':r.randint(40,100), 'comfort':r.randint(0,10)} for car in range(1, cars_total+1)}


	def print_passengers(self):
		"""Виведення кількості пасажирів"""
		print(Passengers(name=self.name, cars=self.cars))

	def print_baggage(self):
		"""Виведення кількості всього багажу"""
		print(Baggage(name=self.name, cars=self.cars))

	def print_comfort(self):
		"""Виведення вагонів за степенем комфорту"""
		print(Comfort_of_Cars(name=self.name, cars=self.cars))

	def find_car_by_passengers(self, start, end):
		"""Пошук вагонів, в яких кількість пасажирів задовільняє заданий діапазон"""
		amount = 0
		print("\nSuitable cars for your request:\n")
		for i in self.cars:
			if self.cars[i]['passengers'] >= start and  self.cars[i]['passengers'] <= end:
				amount +=1
				print("Car {num}: passengers - {passengers}.".format(num=i, passengers= self.cars[i]['passengers']))
		if amount == 0: print("There is no car with the number of passengers that is in your range")

		

if __name__ == '__main__':
	train = Train()
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
	#Міняю про всяк випадок початок і кінець, якщо було задано навпаки
	if start > end: start, end = end, start
	print(train)
	print("----------------")
	train.print_passengers()
	print("----------------")
	train.print_baggage()
	print("----------------")
	train.print_comfort()
	print("----------------")
	train.find_car_by_passengers(start=start, end=end)

