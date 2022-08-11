import os
import tableout

try:
	from colorama import init
except:
	os.system('pip install colorama')
	from colorama import init

init()
from colorama import Fore, Back

def cls():
	os.system('cls || clear')

class Player:
	def __init__(self):
		self.hp = 100
		self.strength = 5
		self.agility = 0
		self.money = 100
		self.level = 0
		self.xp = 0

		self.weapon = {
			'name': 'Палка',
			'damage': 10,
			'cost': 5
		}
		self.armor = {
			'head': {
				'name': 'Ничего',
				'defense': 0,
				'cost': 0,
				'sellable': False
			},
			'chest': {
				'name': 'Ничего',
				'defense': 0,
				'cost': 0,
				'sellable': False
			},
			'leggings': {
				'name': 'Ничего',
				'defense': 0,
				'cost': 0,
				'sellable': False
			},
			'boots': {
				'name': 'Ничего',
				'defense': 0,
				'cost': 0,
				'sellable': False
			}
		}
	def getDefense():
		return self.weapon['head']['defense'] + self.weapon['chest']['defense'] + self.weapon['leggings']['defense'] + self.weapon['boots']['defense'] + self.agility

shop = {
	'weapon': [{'name': 'Палка', 'damage': 10, 'cost': 5}, {'name': 'Деревянный меч', 'damage': 15, 'cost': 10}],

	'head': [{'name': '', 'damage': , 'cost': }], [{'name': '', 'damage': , 'cost': }]

	'chest': [{'name': '', 'damage': , 'cost': }], [{'name': '', 'damage': , 'cost': }]

	'leggings': [{'name': '', 'damage': , 'cost': }], [{'name': '', 'damage': , 'cost': }]

	'boots': [{'name': '', 'damage': , 'cost': }], [{'name': '', 'damage': , 'cost': }]
}