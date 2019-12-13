data = []
count = 0
len_reviews_sum = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		len_reviews_sum = len_reviews_sum + len(line)
		count += 1
		if count % 1000 == 0:
			print(count)

print('檔案讀取完了,總共有', len(data), '筆留言')
print('留言平均長度為： ', len_reviews_sum / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '筆留言長度小於100')
print(new[0])