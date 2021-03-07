# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:21:40 2018

@author: user
"""

import numpy as np#載入NumPy函式庫
import matplotlib.pyplot as plt#載入Matpltlib函式庫
import math #載入math函式庫

#定義原始方程式
def fn(x):
    y = math.sin(math.pi*x)+math.cos(2*math.pi*x)
    return y;

#原始方程式之二次微分
def fn_diff(x):
    y = -math.pi*math.pi*math.sin(math.pi*x) + 4*math.pi*math.pi*math.cos(2*math.pi*x)
    return y;

#使用Fuzzy逼近的計算
def fuzzy_calculate(x,X_degree):
    #for j in range(len(x)):
        for i in range(len(X_degree)):
            if X_degree[i] > x:
                break;
        Fire_R1_value = 1-((x-X_degree[i-1])/(X_degree[i]-X_degree[i-1]))
        Fire_R2_value = 1-((x-X_degree[i])/(X_degree[i-1]-X_degree[i]))
        molecule = fn(X_degree[i-1])*Fire_R1_value + fn(X_degree[i])*Fire_R2_value
        Denominator = Fire_R1_value + Fire_R2_value
        Final_fn = molecule / Denominator
        return Final_fn;
    
#建立x軸之個數
def x_number(start,stop,step):
    x = {}
    x['x'] = np.arange(start,stop,step)
    x['x_num'] = int((stop - start)/step)
    return x;

#建立原始方程式正確的輸出值
def g_function(x,x_num):
    g = np.zeros(x_num)
    for i in range(len(x)):
        g[i] = fn(x[i])
    return g;

#尋找原始方程式微分二次後之最大值
def g_diff(x,x_num):
    g_diff = np.zeros(x_num)
    for i in range(len(x)):
        temp = fn_diff(x[i])
        g_diff[i] = abs(temp)
    g_diff_max = max(g_diff)
    return g_diff_max;

#主程式
start = -1
stop = 1
step = 0.01
Epsilon = 0.1

x = x_number(start,stop,step)
g = g_function(x['x'],x['x_num'])
g_diff_max = g_diff(x['x'],x['x_num'])

h1_square = Epsilon/g_diff_max*8
h1 = h1_square**(1/2)
Total_rule_num = 2/h1
Total_rule_num2 = int(Total_rule_num)
if Total_rule_num > Total_rule_num2:
    Total_rule_num2 = Total_rule_num2+2
    Total_rule_num = Total_rule_num2

X_degree = np.zeros((Total_rule_num,1))
for i in range(Total_rule_num):
    X_degree[i] = -1+i*h1


fuzzy_fn = np.zeros(len(x['x']))
x_temp = x['x']
for j in range(len(x_temp)):
    fuzzy_fn[j] = fuzzy_calculate(x_temp[j],X_degree)
    
fig = plt.figure()
plt.plot(x['x'],g, c='r',marker='o')
plt.plot(x['x'],fuzzy_fn, c='b',marker='x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('g(x)-f(x) comparision');
plt.show()
print('OK')