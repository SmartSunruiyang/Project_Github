# 求中位数
def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2] + data[n//2 - 1]) / 2, sum(data) / 2, (sum(data) / 2) + 1
    else:
        return data[(n + 1) // 2]


# 求众数
def mode(data):
    count = 0
    mode_num = 0
    mode_num_list = []
    for item in data:
        if data.count(item) > count:
            count = data.count(item)
    # 如果有其他数跟众数出现的次数相同，则返回众数的列表
    for item in data:
        if data.count(item) == count:
            mode_num_list.append(item)
    return list(set(mode_num_list))


# 求平均数
def mean(data):
    return sum(data) / len(data)


# 求方差
def variance(data):
    mean_value = mean(data)
    value_list = []
    for item in data:
        value_list.append((item - mean_value) ** 2)
    return sum(value_list) / len(data)


# 求标准差
def standard_deviation(data):
    return variance(data) ** 0.5


# 求频率-求每个数对于整个数组出现的次数
def frequency_group(data):
    frequency_list = []
    for item in data:
        frequency_list.append(data.count(item)/len(data))
    return dict(zip(data, frequency_list))


# 求频率-求每个数对于数组总和的比例
def frequency_sum(data):
    frequency_list = []
    for item in data:
        frequency_list.append(item/sum(data))
    return dict(zip(data, frequency_list))


# 调用所有函数并格式化输出
def main(data):
    print('您输入的数组是：', data)
    print('数组总和是：', sum(data))
    print('数组的最大数是：', max(data))
    print('数组的最小数是：', min(data))
    print('数组正序排列是：', sorted(data))
    print('数组倒序排列是：', sorted(data, reverse=True))
    print('中位数是(第一个是数组的中位数，剩余的是数组总和的中位数)：', median(data))
    print('众数是：', mode(data))
    print('平均数是：', mean(data))
    print('方差是：', variance(data))
    print('标准差是：', standard_deviation(data))
    print('频率-每个数对于整个数组出现的次数：', frequency_group(data))
    print('频率/百分比-每个数对于数组总和的比例：', frequency_sum(data))


# 由样本估计总体数据
def reverse_mode():
    while True:
        data = list(input('输入数据 q退出（顺序为：样本数据，样本总数量，总体数量! 否则输出将异常）：').split(' ' or ',' or '，' or ';'))
        if data[0] == 'q':
            break
        else:
            try:
                data = list(map(int, data))
                print(data[0] * data[2] / data[1], '\n', '-' * 50)
            except Exception as exc:
                print(exc, ' ; 输入错误！请输入数字！数字数量只能为3个！')
                continue






string = '''     _______.___________.    ___   .___________. __       _______.___________. __    ______   .___________.  ______     ______    __          _______.   
    /       |           |   /   \  |           ||  |     /       |           ||  |  /      |  |           | /  __  \   /  __  \  |  |        /       |   
   |   (----`---|  |----`  /  ^  \ `---|  |----`|  |    |   (----`---|  |----`|  | |  ,----'  `---|  |----`|  |  |  | |  |  |  | |  |       |   (----`   
    \   \       |  |      /  /_\  \    |  |     |  |     \   \       |  |     |  | |  |           |  |     |  |  |  | |  |  |  | |  |        \   \       
.----)   |      |  |     /  _____  \   |  |     |  | .----)   |      |  |     |  | |  `----.      |  |     |  `--'  | |  `--'  | |  `----.----)   |      
|_______/       |__|    /__/     \__\  |__|     |__| |_______/       |__|     |__|  \______| _____|__|      \______/   \______/  |_______|_______/       
                                                                                            |______|                                                     '''
print(f'{string}\ntype "help" to get help document')
# 用户输入，数据检查
while True:
    default_list = list(input(f'{"-" * 50}\nEnter the info（r to cycle/q to quit）：').split(' ' or ',' or '，' or ';'))
    if default_list[0].lower() == 'r':
        continue
    elif default_list[0].lower() == 'q':
        print('欢迎下次使用statistic_tools！')
        break
    elif default_list[0].lower() == 'help':
        print('statistic_tools.py\n'
              '输入数组，输出数组的最大数、最小数、正序排列、倒序排列、中位数、众数、平均数、方差、标准差\n'
              '输入r，重新输入\n'
              '输入q，退出程序\n'
              '输入help，获取帮助文档\n'
              '输入version，获取版本号\n'
              '输入reverse，由样本数据逆向估算总体数据\n'
              '所有输入的数组中可以使用空格、逗号、分号分隔，前后不能有空格\n')
        continue
    elif default_list[0].lower() == 'version':
        print('statistic_tools.py -version 1.0\n')
        continue
    elif default_list[0].lower() == 'reverse':
        reverse_mode()
        continue
    else:
        try:
            num_list = list(map(int, default_list))
            if len(num_list) == 1:
                print('数组不能只输入一个数字！', '\n', '*' * 50)
                continue
        except Exception as e:
            print(e, ' ; 输入的数据有误，请重新输入！')
            continue
        else:
            main(num_list)
            default_list.clear()

