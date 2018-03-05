# 2018年江苏刑侦推理题
import random, time
# 表达式select[answer]指的是该题自身的答案
# 表达式inputs[select[answer]]指的是答案中答案（题目）的答案
def judge(inputs):
	answer = [int(_) for _ in inputs]
	select2 = '2301'
	# 第2题的答案就是第五题的答案
	if select2[answer[1]] != inputs[4]:
		return False
	select3 = '2513'
	# 第3题的答案里，与剩余的其它三个选项对应题目的案应该不同
	temp = select3.replace(select3[answer[2]], '')  # 第三题正确选项外的剩余的答案
	if inputs[int(select3[answer[2]])] in [inputs[int(i)] for i in temp]:
		return False
	# 第4题的答案里，对应的两个题目的答案应该相同
	select4 = [(0, 4), (1, 6), (0, 8), (5, 9)]
	if inputs[int(select4[answer[3]][0])] != inputs[int(select4[answer[3]][1])]:
		return False
	select5 = '7386'
	# 第5题的案例里，对应的题目的答案应该等于第5题自身的答案
	if inputs[int(select5[answer[4]])] != inputs[4]:
		return False
	select6 = [(1, 3), (0, 5), (2, 9), (4, 8)]
	# 第6题的案例里，对应的题目的答案应该等于第8题自身的答案
	if inputs[select6[answer[5]][0]] != inputs[7] or inputs[select6[answer[5]][1]] != inputs[7]:
		return False
	select7 = '2103'
	# 第7题自身的答案，应该等于所有题目里选项最少的答案
	minAnswerCount = min('0123', key=inputs.count)
	maxAnswerCount = max('0123', key=inputs.count)
	if select7[answer[6]] != minAnswerCount:
		return False
	select8 = '6419'
	# 第8题自身的答案，应该和第一题的答案不相邻
	if abs(int(select8[answer[7]]) - int(inputs[0])) == 1:
		return False
	select9 = '5918'
	# 第9题的答案里，对应的题目的答案与第5题自身的答案相同的真假性为flag
	flag = inputs[int(select9[answer[8]])] == inputs[4]
	# flag与第1题和第6题的答案相同为互斥条件
	if(inputs[0] == inputs[5]) == flag:
		return False
	select10 = '3241'
	# 第10题的答案，应该等于ABDC出现的最多次数-出现的最少次数
	if (inputs.count(maxAnswerCount) - inputs.count(minAnswerCount)) != int(select10[answer[9]]):
		return False
	return True
if __name__ == "__main__":
	time_conut, time_start = 0, time.time()
	while True:
		inputs = ''
		time_conut += 1
		for i in range(10):
			inputs += str(random.choice([0, 1, 2, 3]))
		if judge(inputs) is True:
			print('经过穷举{}次后，答案为：{}'.format(time_conut, ''.join([chr(65 + int(i)) for i in inputs])))
			break
	print('程序消耗时间为：{}'.format(time.time() - time_start))
