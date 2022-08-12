import os
import json
import tableout as tablo

def dumpSave():
	with open('data.json', 'w') as file:
		json.dump(data, file)

with open('data.json', 'r') as df:
	data = json.load(df)

if data['settings']['coloredOutput'] == 'true' or data['settings']['coloredOutput'] == 'forcedFalse':
	try:
		from colorama import init
		init()
		from colorama import Fore, Back
	except:
		try:
			os.system('pip install colorama')
			from colorama import init
			init()
			from colorama import Fore, Back
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

def getPlayerDefense():
	return data['player']['armor']['head']['defense'] + data['player']['armor']['chest']['defense'] + data['player']['armor']['leggings']['defense'] + data['player']['armor']['boots']['defense'] + data['player']['skills']['agility']

def healPlayer(self, hp):
	self.hp += hp
	if self.hp > self.maxHp:
		self.hp = self.maxHp

def killPlayer(self):
	pass

def hurtPlayer(self, hp):
	self.hp -= hp
	if self.hp <= 0:
		self.kill()

def xpToNextLevel(self):
	return 25 * 1.5 ^ (self.level)

shop = {
	'weapon': [
		{'name': 'Деревянный меч', 'damage': 15, 'cost': ²0, 'minLevel': 0},
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
		'enemies': [0, 1],
	},
	{
		'name': 'Гоблинский город',
		'enemies': [0, 1, 2, 3],
	},
	{
		'name': 'Центр города',
		'enemies': [2, 3, 4, 5],
	},
]

cls()
# Main menu
print(f'=== GOBLIN RPG ===')