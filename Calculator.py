import os
import time
from pyfiglet import Figlet
from colorama import *

def Calculator_V1():

	if os.name == 'nt':

		f = Figlet(font='standard')
		
		while True:
			print(f.renderText('CALCULATOR'))
			print("")
			x=int(input("Введите первое число: "))
			y=int(input("Введите второе число: "))
			print(" ")
			print("Результаты:")
			print(Fore.GREEN + x + y + Style.RESET_ALL)
			os.system('pause')
			os.system('cls')

	else:
		print(Fore.RED + "Ваша операционная система не поддерживается!" + Style.RESET_ALL)
		time.sleep(2)
		os.system('clear')
		exit()

Calculator_V1()