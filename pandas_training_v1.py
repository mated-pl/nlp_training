import pandas as pd, numpy as np
# s1 = pd.Series()
# print(s1)
#
# a1 = np.array([1,2,3,4])
# print(a1)
#
# s2 = pd.Series(a1)
# print(s2)
#
# s3 = pd.Series(a1, index=[100,101,102,103])
# print(s3)
#
# d1 = {'a' : 0., 'b' : 1., 'c' : 2.}
# print(d1)
# s4 = pd.Series(d1)
# print(s4)
#
# s5 = pd.Series(3)
# print(s5)
#
# s6 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# print(s6)
# print(s6[:1])
# print(s6['a'])

l1 = [1,2,3,4,5]
df = pd.DataFrame(l1)
print(df)

l2 = [['Alex',10],['Bob',12],['Clarke',13]]
df2 = pd.DataFrame(l2,columns=['Name','Age'])
print(df2)