import random
start = input('請決定開始值= ')
end = input('請決定結束值= ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	num = input('請猜猜數字~')
	num = int(num)
	count += 1 #count  = count + 1
	if num == r:
		print('你猜對了! ')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
