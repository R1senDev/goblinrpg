import sys

ss = {
	'tdBorder': '│',
	'rlBorder': '─',
	'rdBorder': '┌',
	'dlBorder': '┐',
	'trBorder': '└',
	'tlBorder': '┘',
	'rdlBorder': '┬',
	'tdlBorder': '┤',
	'trlBorder': '┴',
	'trdBorder': '├',
	'trdlBorder': '┼',

	'tick': '✓',
	'cross': '✘',

	'ellipsis': '…'
}

def printTable(table):
	maxColumns = []
	for col in zip(*table):
		lenEl = []
		[lenEl.append(len(el)) for el in col]
		maxColumns.append(max(lenEl))

	sys.stdout.write(ss['rdBorder'])
	for ml in range(len(maxColumns)):
		sys.stdout.write(ss['rlBorder'] * (maxColumns[ml] + 2))
		if ml != len(maxColumns) - 1:
			sys.stdout.write(ss['rdlBorder'])
		else:
			print(ss['dlBorder'])

	for m, el in enumerate(table):
		for n, col in enumerate(el):
			sys.stdout.write(f'{ss["tdBorder"]} {col:{maxColumns[n] + 1}}')
		print(ss['tdBorder'])
		if m != len(table) - 1:
			sys.stdout.write(ss['trdBorder'])
			for ml in range(len(maxColumns)):
				sys.stdout.write(ss['rlBorder'] * (maxColumns[ml] + 2))
				if ml != len(maxColumns) - 1:
					sys.stdout.write(ss['trdlBorder'])
				else:
					print(ss['tdlBorder'])

	sys.stdout.write(ss['trBorder'])
	for ml in range(len(maxColumns)):
		sys.stdout.write(ss['rlBorder'] * (maxColumns[ml] + 2))
		if ml != len(maxColumns) - 1:
			sys.stdout.write(ss['trlBorder'])
		else:
			print(ss['tlBorder'])