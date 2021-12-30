import random      # 导入库
import time

while True:        # 将随机取得的408个二进制数存入列表
    num_list = []
    for i in range(408):
        numbers = random.randint(0, 1)
        num_list.append(numbers)
    num_print = map(str, num_list)     # 使用map()函数将类型全部改为字符串
    result = ''.join(num_print)        # 使用''.join()语句将列表内的所有元素取出并连接
    time.sleep(0.07)
    print(f"\033[0;32;40m{result}\033[0m")
