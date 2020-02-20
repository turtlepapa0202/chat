
# 讀取function
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8') as f:
								# 若遇到怪符號，要變成'utf-8-sig'
		for line in f:
			chat.append(line.strip())
	return chat


# 轉換function，看看每個人講了幾個字
def convert(chat):
	line_chat = []
	choe_count = 0
	choe_sticker_count = 0
	choe_image_count = 0
	kuo_count = 0
	kuo_sticker_count = 0
	kuo_image_count = 0
	for line in chat:
		line_chat = line.strip().split(' ')
		print(line_chat)
		if line_chat[1] == '可誼鼠誼喵誼':
			if line_chat[2] == '貼圖':
				choe_sticker_count += 1
			elif line_chat[2] == '圖片':
				choe_image_count += 1
			else:
				for words in line_chat[2:]:
					choe_count += len(words)
		elif line_chat[1] == 'En-Lin':
			if line_chat[3] == '貼圖':
				kuo_sticker_count += 1
			elif line_chat[3] == '圖片':
				kuo_image_count += 1
			else:
				for words in line_chat[3:]:
					kuo_count += len(words)
	print('可誼鼠誼喵誼說了', choe_count, '個字')
	print('傳了', choe_sticker_count, '次貼圖')
	print('傳了', choe_image_count, '次圖片')
	print('En-Lin Kuo說了', kuo_count, '個字')
	print('傳了', kuo_sticker_count, '次貼圖')
	print('傳了', kuo_image_count, '次圖片')
	

# 寫入function
def write_file(filename, new_chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for c in new_chat:
			f.write(c + '\n')

def main():
	chat = read_file('[LINE]可誼鼠誼喵誼.txt')
	convert(chat)
	# new_chat = convert(chat)
	# print(new_chat)
	# write_file('output.txt', new_chat)
main()