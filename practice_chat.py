
# 讀取function
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8') as f:
								# 若遇到怪符號，要變成'utf-8-sig'
		for line in f:
				chat.append(line.strip())
	return chat

# 轉換function
def convert(chat):
	new_chat = []
	person = None # person = 'nobody'
				  # None：虛無，person沒有value
	for line in chat: 
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:   # if person != 'nobody'
					 # person要有值才是True
			new_chat.append(person + ':' + line) # 太聰明了...
		# print(new_chat) # 一行一行印出來
	return new_chat

# 寫入function
def write_file(filename, new_chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for c in new_chat:
			f.write(c + '\n')

def main():
	chat = read_file('input.txt')
	new_chat = convert(chat)
	print(new_chat)
	write_file('output.txt', new_chat)
main()