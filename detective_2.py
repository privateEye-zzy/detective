import random, time
def judge(answer, n):
    # 问题一：n小于500吗？已知回答为假
    if answer[0] is True and n < 500:
        return False
    if answer[0] is False and n > 500:
        return False
    # 问题二：n是平方数吗？已知回答为假
    if answer[1] is True and n in arr2:
        return False
    if answer[1] is False and n not in arr2:
        return False
    # 问题三：n是立方数吗？已知回答为真
    if answer[2] is True and n not in arr3:
        return False
    if answer[2] is False and n in arr3:
        return False
    # 问题四：n的倒数第二位数字是1吗？已知回答可能为真也可能为假
    if answer[3] is True and int(str(n)[-2]) != 1:
        return False
    if answer[3] is False and int(str(n)[-2]) == 1:
        return False
    return True
arr2, arr3 = [], []
[arr2.append(i**2) for i in range(1, 1301) if i**2 >= 13 and i**2 <= 1300]
[arr3.append(i**3) for i in range(1, 1301) if i**3 >= 13 and i**3 <= 1300]
if __name__ == "__main__":
    time_conut, time_start = 0, time.time()
    while True:
        time_conut += 1
        answer = [False, False, True, random.choice([True, False])]
        n = random.randint(13, 1300)
        if judge(answer=answer, n=n) is True:
            print('经过穷举{}次后，对方的回答为：{}，正真的房间号为：{}'.format(time_conut, answer, n))
            break
    print('程序消耗时间为：{}'.format(time.time() - time_start))
