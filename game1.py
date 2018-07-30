'''
散户与庄家之间的博弈
'''
import numpy as np
import matplotlib.pyplot as plt
def draw(xs, ys, es):
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    plt.ylabel('Profit')
    plt.title('Buyer Profit change')
    ax1.plot(xs, ys, color='red')
    ax2 = fig.add_subplot(122)
    plt.ylabel('Expect')
    plt.title('Buyer Expect change')
    ax2.plot(xs, es, color='green')
    plt.show()
# 庄家策略，1：拉升股价，0：打压股价
def get_result_banker(y):
    return 1 if np.random.random() <= y else 0
# 散户策略，1：买多，0：买空
def get_result_buyer(x):
    return 1 if np.random.random() <= x else 0
if __name__ == '__main__':
    mouths, days = 12 * 2, 30  # 月数和天数
    profit = 10.0  # 散户成本
    ys, es = [], []
    for i in range(mouths):
        for j in range(days):
            a, b = 1 / 3, 2 / 5  # 庄家计算不等式的解
            y = (b - a) * np.random.random() + a  # 庄家的策略
            x = np.random.random()  # 散户的策略
            r1 = get_result_buyer(x=x)
            r2 = get_result_banker(y=y)
            # 如果庄家拉升股价，散户买多，则散户获得高收益
            if r1 == 1 and r2 == 1:
                profit += 3
            # 如果庄家打压股价，散户买空，则散户获得低收益
            elif r1 == 0 and r2 == 0:
                profit += 1
            # 如果庄家打压股价，散户买多，或者庄家拉升股价，散户买空，则散户亏损
            else:
                profit -= 2
        E = 3 * x * y + (1 - x) * (1 - y) - 2 * x * (1 - y) - 2 * (1 - x) * y  # 买家期望
        es.append(E)
        ys.append(profit)
    draw(list(range(mouths)), ys=ys, es=es)
