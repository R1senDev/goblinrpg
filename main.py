import os
import tableout as tablo

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
        self.maxHp = 100
		self.hp = 100
		self.strength = 5
		self.agility = 0
		self.money = 20
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

    def heal(self, hp):
        self.hp += hp
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def kill(self):
        pass

    def hurt(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.kill()

shop = {
	'weapon': [
        {'name': 'Палка', 'damage': 10, 'cost': 5, 'minLevel': 0},
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
        'damage': [8, 11],
        'defense': [0, 0],
        'reward': [5, 10]
    },
    {
        'name': 'Гоблин-громила',
        'hp': 100,
        'damage': [10, 12],
        'defense': [0, 1],
        'reward': [5, 15]
    },
    {
        'name': 'Гоблин-ловкач',
        'hp': 100,
        'damage': [6, 9],
        'defense': [5, 7],
        'reward': [10, 15]
    }
    {
        'name': 'Гоблин-страж',
        'hp': 100,
        'damage': [10, 15],
        'defense': [0, 1],
        'reward': [10, 20]
]

locations = [
    {
        'name': 'Заброшенная шахта',
        'enemies': [0, 1]
    },
    {
        'name': 'Гоблинский город',
        'enemies': [0, 1, 2, 3]
]
