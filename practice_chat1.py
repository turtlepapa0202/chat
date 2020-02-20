

with open('3.txt', 'r', encoding='utf-8') as f:
	chat = []
	for line in f:
		chat.append(line.strip())

new_chat = []
for line in chat:
	r = line.strip().split(' ')
	new_chat.append([r[0][:5], r[0][5:], r[1:]])
	# print(new_chat)
print(new_chat)


with open('4.csv', 'w', encoding='utf-8') as f:
	for line in new_chat:
		# print(line)
		line = str(line)
		f.write(line + '\n')