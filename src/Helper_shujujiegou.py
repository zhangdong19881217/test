#python 数据结构
import os
'''
---------------------列表-----------------------------------------------------------
a = [66.25, 333, 333, 1, 1234.5]
list.append(x) 	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L) 	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x) 	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x) 	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i]) 	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear() 	移除列表中的所有项，等于del a[:]。
list.index(x) 	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x) 	返回 x 在列表中出现的次数。
list.sort() 	对列表中的元素进行排序。
list.reverse() 	倒排列表中的元素。
list.copy() 	返回列表的浅复制，等于a[:]。 
---------------------元组-----------------------------------------------------------
元组由若干逗号分隔的值组成，例如：
t = 12345, 54321, 'hello!'
t[0]
12345
t
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
---------------------集合-----------------------------------------------------------
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 删除重复的
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # 检测成员
True
'crabgrass' in basket
False

# 以下演示了两个集合的操作

a = set('abracadabra')
b = set('alacazam')
a                                  # a 中唯一的字母
{'a', 'r', 'b', 'c', 'd'}
a - b                              # 在 a 中的字母，但不在 b 中
{'r', 'd', 'b'}
a | b                              # 在 a 或 b 中的字母
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # 在 a 和 b 中都有的字母
{'a', 'c'}
a ^ b                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
{'r', 'd', 'b', 'm', 'z', 'l'}
---------------------字典-----------------------------------------------------------
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
tel['jack']
4098
del tel['sape']
tel['irv'] = 4127
tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
list(tel.keys())
['irv', 'guido', 'jack']
sorted(tel.keys())
['guido', 'irv', 'jack']
'guido' in tel
True
'jack' not in tel
False
'''

class CHelper_shujujiegou(object):
    def __init__(self): 
        pass 
    def test(self):

        return "null"
