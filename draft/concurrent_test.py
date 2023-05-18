import concurrent.futures

# 定义一个任务执行函数
def task(number):
    return number ** 2, number ** 3

# 创建一个线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    to_do = [executor.submit(task, i) for i in range(1, 6)]

# 等待所有任务完成，并获取它们的结果列表
results = []
for future in concurrent.futures.as_completed(to_do):
    results.append(future.result())

# 显示结果列表中的返回值
for r in results:
    print(type(r))
    print(r[0])
    print(r)
