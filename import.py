import random

# 这里就是把random这个module载入进去

r = random.randint(1, 100)

# 这里的.其实就是'的'的意思
# 也就是我们从random这个module中提取出randint进行使用
# 这里面(1, 100)就是从1到100里面随机产生整数
# 所以总结起来说就是
# 我从random这个module里面提取出randint这个产生随机数的工具进行使用
# 同时我给这个工具设成产生的随机数在1到100之间，然后把产生的数存进r
# 提醒一下，这里1和100是包括在里面的

print(r)