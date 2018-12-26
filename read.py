data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1 #讀取一筆留言就計數1
		data.append(line)
		if count % 100000 == 0:#顯示讀取每10萬筆
			print(len(data))
print('讀取完畢總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均留言長度:', sum_len/len(data))

#篩選留言數小於100的留言
new = []
for d in data :
	if len(d) < 100 :
		new.append(d)
print('有', len(new), '筆資料留言字數小於100')