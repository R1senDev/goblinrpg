import os
import json
from random import randint, choice
import tableout as tout

def dumpSave():
	with open('data.json', 'w') as file:
		json.dump(data, file)

with open('data.json', 'r') as df:
	data = json.load(df)

if data['settings']['coloredOutput'] == 'true' or data['settings']['coloredOutput'] == 'forcedFalse':
	try:
		from colorama import init
		init()
		from colorama import Fore, Back, Style
	except:
		try:
			os.system('pip install colorama')
			from colorama import init
			init()
			from colorama import Fore, Back, Style
		except:
			data['settings']['coloredOutput'] = 'forcedFalse'

dumpSave()

def cls():
	if data['settings']['os'] == 'mc':
		os.system('cls || clear')
	elif data['settings']['os'] == 'linux':
		os.system('clear')
	elif data['settings']['os'] == 'windows':
		os.system('cls')

def getPlayerDamage():
	return data['player']['weapon']['damage'] + data['player']['skills']['strength']

def getPlayerDefense():
	return data['player']['armor']['head']['defense'] + data['player']['armor']['chest']['defense'] + data['player']['armor']['leggings']['defense'] + data['player']['armor']['boots']['defense'] + data['player']['skills']['agility']

def healPlayer(self, hp):
	data['player']['hp'] += hp
	if data['player']['hp'] > data['player']['maxHp']:
		data['player']['hp'] = data['player']['maxHp']

def hurtPlayer(self, hp):
	data['player']['hp'] -= hp
	if data['player']['hp'] <= 0:
		self.kill()

def killPlayer(self):
	pass

def xpToNextLevel(self):
	return 25 * 1.5 ^ (data['player']['level'])

class Enemy:
	__init__(self, avaliableIds):
		self.id = choice(avaliableIds)
		self.hp = mobs[self.id]['hp']
		self.damage = choice(mobs[self.id]['damage'])
		self.defense = choice(mobs[self.id]['defense'])

	def hit(self):
		self.hp -= getPlayerDamage()
		if randint(1, 100) <= data['player']['skills']['accuracy']:
			self.hp -= getPlayerDamage()
		if self.hp <= 0:
			self.hp = 0
			self.kill()

	def kill(self):
		pass

currentEnemy = None

shop = {
	'weapon': [
		{'name': 'Деревянный меч', 'damage': 15, 'cost': 20, 'minLevel': 0},
		{'name': 'Ржавый нож', 'damage': 20, 'cost': 50, 'minLevel': 2},
	],

	'head': [
		{'name': 'Деревянный шлем', 'defense': 2, 'cost': 20, 'minLevel': 2}
	],

	'chest': [
		{'name': 'Деревянный нагрудник', 'defense': 3, 'cost': 30, 'minLevel': 2}
	],

	'leggings': [
		{'name': 'Деревянные поножи', 'defense': 2, 'cost': 20, 'minLevel': 2}
	],

	'boots': [
		{'name': 'Деревянные ботинки', 'defense': 1, 'cost': 10, 'minLevel': 2}
	]
}

# List of all mobs existing in game
mobs = [
	{
		'name': 'Гоблин-рекрут',
		'hp': 100,
		'damage': [5, 10],
		'defense': [0, 0],
		'reward': {'coins': [5, 10], 'xp': [10, 20]}
	},
	{
		'name': 'Гоблин-громила',
		'hp': 100,
		'damage': [10, 12],
		'defense': [0, 1],
		'reward': {'coins': [5, 15], 'xp': [10, 25]}
	},
	{
		'name': 'Гоблин-ловкач',
		'hp': 100,
		'damage': [6, 9],
		'defense': [5, 7],
		'reward': {'coins': [10, 15], 'xp': [15, 25]}
	},
	{
		'name': 'Гоблин-страж',
		'hp': 100,
		'damage': [10, 15],
		'defense': [0, 1],
		'reward': {'coins': [10, 20], 'xp': [20, 30]}
	},
	{
		'name': 'Гоблин-убийца',
		'hp': 100,
		'damage': [15, 20],
		'defense': [0, 0],
		'reward': {'coins': [15, 25], 'xp': [20, 35]}
	},
	{
		'name': 'Гоблин в доспехах',
		'hp': 100,
		'damage': [2, 5],
		'defense': [5, 20],
		'reward': {'coins': [15, 30], 'xp': [25, 35]}
	},
]

locations = [
	{
		'name': 'Заброшенная шахта',
		'level': 0,
		'enemies': [0, 1],
	},
	{
		'name': 'Гоблинский город',
		'level': 2,
		'enemies': [0, 1, 2, 3],
	},
	{
		'name': 'Центр города',
		'level': 5,
		'enemies': [2, 3, 4, 5],
	},
]

cls()
print(f'=== GOBLIN RPG ===\n\n[1] Продолжить\n[2] Новая игра\n[3] Настройки\n\n[0] Выход')
inp = input('Введи номер пункта, который хочешь выбрать: ')

cls()
if inp == '1':
	print('Куда отправимся?\n\n[1] Сражаться\n[2] Магазин\n[3] О герое\n[4] Настройки\n[0] Главное меню\n\nВведи номер пункта, который хочешь выбрать: ')
	inp = input('Введи номер пункта, который хочешь выбрать: ')
	if inp = '1':
		print('Выбери локацию:')
		for loc in range(len(locations)):
			if data['player']['level'] >= locations[loc]['level']:
				print(f'[{loc + 1}] {locations[loc]['name']}')
				maxLocationId = loc + 1
			else:
				print(f'    {locations[loc]['name']} (Откроется на уровне {locations[loc]['level']})')
				break
		inp = input('\nВведи номер пункта, который хочешь выбрать: ')
		if int(inp) <= maxLocationId:
			currentLocation = int(inp) - 1
			while inp != '0':
				currentEnemy = Enemy(locations[currentLocation]['enemies'])
				print(f'БИТВА!\n{'=' * 10}\nАктивные эффекты:')
				for effect in data['player']['effects']:
					print(f'{effect['name']} {effect['value']}')
				print(f'{'=' * 10}\n{tout.printTable([[]])}')
		else:
			# Incorrect input warning
			pass

elif inp == '2':
	if data['settings']['coloredOutput'] == "true":
		inp = input(f'Чтобы начать новую игру, введи следующую фразу:\n\n{Fore.YELLOW}{Style.BRIGHT}Начиная новую игру, я понимаю, что весь мой прогресс будет потерян по причине перезаписи файла сохранения. Также я подтверждаю, что ознакомлен с политикой конфиденциальности, изложенной в файле privacy.md и поставляющейся вместе с данной программой. Ахаллай-махаллай, сим-салабим, сохранянус-удалянус.{Style.NORMAL}{Fore.WHITE}\n\n')
		if inp == 'Начиная новую игру, я понимаю, что весь мой прогресс будет потерян по причине перезаписи файла сохранения. Также я подтверждаю, что ознакомлен с политикой конфиденциальности, изложенной в файле privacy.md и поставляющейся вместе с данной программой. Ахаллай-махаллай, сим-салабим, сохранянус-удалянус.':
			pass

elif inp == '4':
	print('=== НАСТРОЙКИ ===\nПриятного дня.')

elif inp == '0':
	exit()

elif inp == 'console':
	print('=== КОНСОЛЬ РАЗРАБОТЧИКА ===\n')
	comm = ''
	while comm != 'exit':
		comm = input('>>> ')

		if comm.split(' ')[0] == 'dump':
			dumpSave()
			if data['settings']['coloredOutput'] == "true":
				print(f'dump: {Fore.GREEN}Success{Fore.WHITE}')
			else:
				print('dump: Success')

		elif comm.split(' ')[0] == 'save':
			print(data)

		elif comm.split(' ')[0] == 'effect':
			if comm.split(' ')[1] == 'add':
				data['player']['effects'][comm.split(' ')[2]] = comm.split(' ')[3]
			elif comm.split(' ')[1] == 'remove':
				data['player']['effects'][comm.split(' ')[2]] = 0
			elif comm.split(' ')[1] == 'descrease':
				data['player']['effects'][comm.split(' ')[2]] -= 1
			elif comm.split(' ')[1] == 'increase':
				data['player']['effects'][comm.split(' ')[2]] += 1

		elif comm.split(' ')[0] == 'skill':
			if comm.split(' ')[1] == 'set':
				data['player']['skills'][comm.split(' ')[2]] = comm.split(' ')[3]
			elif comm.split(' ')[1] == 'reset':
				data['player']['skills'][comm.split(' ')[2]] = 0
			elif comm.split(' ')[1] == 'descrease':
				data['player']['skills'][comm.split(' ')[2]] -= 1
			elif comm.split(' ')[1] == 'increase':
				data['player']['skills'][comm.split(' ')[2]] += 1

		elif comm.split(' ')[0] == 'exit':
			pass

		else:
			print(f'Unknown command "{comm.split(' ')[0]}"')