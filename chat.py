
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f :
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
#把line清單裡的東西印出來，一行一行讀取
		if line == 'Allen':
		#如果line=Allen的話，把現在說話的人叫做Allen
			person = 'Allen'
			continue
		elif line == 'Tom':
			person =' Tom'
			continue
		if person:
		#如果person有值的話
			new.append(person + ':'+ line)
	return new
	#+是合併的意思，人名+:+空格

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()