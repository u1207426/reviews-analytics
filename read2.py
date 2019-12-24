# 讀取檔案
def read_file(filename):
	data = []
	with open(filename, 'r') as f:
		for line in f:
			data.append(line.strip())
	return data

# 建立字數對照dictionary
def word_dic(data):
	wc = {} # word_count
	for d in data:
		words = d.split(' ')
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1 # 新增新的key進字典
	return wc

# 查找字出現次數
def word_count(wc):
	while True:
		word = input('請輸入您要查找的字(輸入q結束程式)： ')
		if word == 'q':
			break
		if word in wc:
			print('您輸入的', word, '共出現', wc[word], '次')
		else:
			print('您輸入的字沒出現過喔！')
	print('感謝使用本功能')

# main
data = read_file('reviews.txt')
wc = word_dic(data)
word_count(wc)