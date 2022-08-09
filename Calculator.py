import os
import time
from pyfiglet import Figlet
from colorama import *

def Calculator_V1():

	def pc():
		os.system('pause')
		os.system('cls')

	if os.name == 'nt':

		f = Figlet(font='standard')
		
		while True:
			print(f.renderText('CALCULATOR'))
			print(" ")
			print(" 1. Сложение")
			print(" 2. Вычитания")
			a=input("Выбирите сложение или вычитания (пример: 1): ")
			x=int(input("Введите первое число: "))
			y=int(input("Введите второе число: "))
			if a=='1':
				print(" ")
				print("Результаты:")
				print(Fore.GREEN)
				print(x + y)
				print(Style.RESET_ALL)
				pc()
			if a=='2':
				print(" ")
				print("Результаты:")
				print(Fore.GREEN)
				print(x - y)
				print(Style.RESET_ALL)
				pc()


	else:
		print(Fore.RED + "Ваша операционная система не поддерживается!" + Style.RESET_ALL)
		time.sleep(2)
		os.system('clear')
		exit()

Calculator_V1()