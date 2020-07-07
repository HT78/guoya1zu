 # a = 65
 # if (a > 0 and a < 60):
 #    print("不及格")
 #
 #
 # if a in range (61,70):
# #     # print("及格")
# s = 1
# # for i in range (10,0,-1):
# #     s *= i
# print(s)



#  定义一个求两个数商和余数的方法:
# def shang_yu(a ,b):
#     if (b == 0):
#         return None
#     else:
#         return (a % b,a // b)
#
#
# res = shang_yu(20,10)
# if res is None:
#     print(res)
#     print("参数错误")
# else:
#     print(res)
#     print("")
#
# #
# a ,*b = (1,2,3,4,5,6)
# def sum1(*args):
#     s = 0
#

# 面对对象
# class calc():
#     a = None
#     b = None
#     res = None
#     def input (self,a,b):
#         self.a = a
#         self.b = b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc() # 类的实例化   c对象
# c.input(20,10)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# 面对对象
# class calc():
#     res = None
#     def __init__(self,a,b):   # 魔法函数，类实例化的时候调用，又称构造方法
#         self.a = a
#         self.b = b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(20,30) # 类的实例化   c对象
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


# # 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",i*j,end ="\t")
#     print()

# 冒号排序
# q =[2,5,5,2,3,9,7,5,6,1,5,263,363,351,0]
# b = len(q)
# for n in range (b-1,0,-1):
#     for m in range (n):
#         if (q [m]>q[m+1]):
#             q[m] , q[m+ 1] = q[m + 1],q[m]
# print(q)
#

# 变量
# class aaa():
#
#     pub_res = "公有变量"
#     __pri_res = "私有变量1"
#     _pri_res= "私有变量2"
#
#     def pub_function(self):
#         print("公有方法")
#     def _pri_function(self):
#         print("私有方法1")
#     def __pri_function(self0):
#         print("私有方法2")
#
# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa().pub_function())
# print(aaa()._pub_function())
# print(aaa().__Pr)



# 继承
# class Parent():
#     money = 10000000
#     house = 100
#     __yi_wu = "裤子"
#     def shou_yi(self):
#         print("点石成金")
# class Child(Parent):
#     ai_hao = "花钱"
#     pass
#
# a = 1,2,3,4,5,6
# # 字符串转变数字
# print(a+int(b))
#
# # 数字转字符串
# print(str(a)+b)
#
# # 字符串转列表  集合  元组
# t = [1,2,3,4]
# y = {5,6,7}
# u = (7,8,9,)
# print(list(y))
# print(set(t))
# print(tuble(u))


# 打开模式: r 读写   w 清空写入  a 追加写入 b  二进制模式
# f = open("aaa.txt",'w' )
# f.write("hello Kitty")
# f.close()

# 下标取顺序
# a = "bgabvlihbanb"
# print(a [0])
# print(a [::-1])

# 格式化
# 通过占位符格式化
# for i range(1,10):
#     for j range(1,i+1)
#         print("%d x %d = %d"%(j,i+j), end="\t")
#     print()


# .format


try:
    f = open ("bbbb.txt",'r')   # 异常
    print(f.read())
    f.close()
except:
    print("文件名不存在")

print("操作完文件")

def div(a,b):
    try:
        return a / b
    except
        return

print(div(10,0))

