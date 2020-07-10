def flatten(n):
    for nn in n:
        for nnn in nn:
            yield nnn

def flatten_recursive(n):

    if not isinstance(n, list):
        yield n
    else:
        for nn in n:
            for nnn in flatten_recursive(nn):
                yield nnn

"""
生成器
1.概念：生成器的一般形式和函数一样，区别在于使用yield返回值，生成器能够
生成多个数值，每次返回一个数值，每次返回之后、冻结，下次调用返回下一个值

2.语法：生成器由两个部分组成，生成器函数和生成器的迭代器
- 生成器函数：包含yield的函数
- 生成器迭代器：取生成器的数值

3.生成器方法
- send()：外部向生成器内发送数据
- throw:  引发异常
- close:  用于停止生成器
"""
if __name__=='__main__':
    nested = [[1, 2, 3, 4], [], [3,4]]
    # 一般的生成器
    iter = flatten(nested)
    for ii in iter:
        print(ii)
    print("---------")
    # 迭代是生成器
    iter2 = flatten_recursive(nested)
    for ii in iter2:
        print(ii)

