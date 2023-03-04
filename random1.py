# 产生一个随机的整数1~100（不要print出来）
# 让使用者重复输入去猜
# 猜对的话 引出'终于猜到了!'
# 猜错的话 要告诉他 比答案大还是小
import random

start = input('请决定随机数字范围的开始值:')
end = input('请决定随机数字范围的结束值')
start = int(start)
end = int(end)

r = random.randint(start, end)
i = 0

while True:
    user = input('请输入你想猜的数字:')
    user = int(user)
    i += 1 # 这个等同于i = i + 1

    if user == r:
        print('终于猜对了！')
        print('你一共猜了', i, '次哦')
        break
    elif user > r:
        print(user, '比它大')
    elif user < r:
        print(user, '比它小')
    print('这是你猜的第', i, '次')
