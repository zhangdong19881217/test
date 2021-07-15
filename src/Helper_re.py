#正则表达式的示例程序
import re

'''
---------------------------------重要点-------------------------------------------------------
re库采用raw string类型表示正则表达式，表示为：r'text'
---------------------------------基本操作-------------------------------------------------------
操作符  	    说明  	                             实例
.           表示任何单个字符  	         
[  ]        字符集，对单个字符给出取值范围  	    [ab]表示a、b，[a-z]表示a到z单个字符    
[^  ]  	    非字符集，对单个字符给出排除范围  	    [^abc]表示非a或b或c的单个字符    
*  	        前一个字符0次或无限次扩展  	            abc* 表示ab、abc、abcc、abccc等    
+  	        前一个字符1次或无限次扩展  	            abc+ 表示abc、abcc、abccc等 
?           前一个字符0次或1次扩展  	            abc  表示 ab、abc    
|  	        左右表达式任意一个  	                abc|def 表示abc、def    
{m}  	    扩展前一个字符m次  	                    ab{2}c表示abbc    
{m,n}  	    扩展前一个字符m至n次（含n）  	        ab{1,2}c表示abc、abbc    
^  	        匹配字符串开头  	                    ^abc表示abc且在一个字符串的开头    
$  	        匹配字符串结尾  	                    abc$表示abc且在一个字符串的结尾    
( )  	    分组标记，内部只能使用| 操作符  	    (abc)表示abc，(abc|def)表示abc、def    
\d  	    数字，等价于[0‐9]  	         
\w  	    单词字符，等价于[A‐Za‐z0‐9_] 
-------------------------------常用函数---------------------------------------------------------
函数  	    说明
re.search()  	    在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象 
        re.search(pattern, string, flags=0) 
        pattern : 正则表达式的字符串或原生字符串表示  
        string : 待匹配字符串    
        flags : 正则表达式使用时的控制标记
re.match()  	    从一个字符串的开始位置起匹配正则表达式，返回match对象  
re.findall()  	    搜索字符串，以列表类型返回全部能匹配的子串  
re.split()  	    将一个字符串按照正则表达式匹配结果进行分割，返回列表类型  
        re.split(pattern, string, maxsplit=0, flags=0)
        输入参数：
        - pattern : 正则表达式的字符串或原生字符串表示
        - string : 待匹配字符串
        - maxsplit: 最大分割数，剩余部分作为最后一个元素输出
        - flags : 正则表达式使用时的控制标记

re.finditer()  	    搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象  
        re.finditer(pattern, string, flags=0)
        pattern : 正则表达式的字符串或原生字符串表示
        string : 待匹配字符串
        flags : 正则表达式使用时的控制标记

re.sub()  	    在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
        re.sub(pattern, repl, string, count=0, flags=0)
        ∙ pattern : 正则表达式的字符串或原生字符串表示
        ∙ repl : 替换匹配字符串的字符串
        ∙ string : 待匹配字符串
        ∙ count : 匹配的最大替换次数
        ∙ flags : 正则表达式使用时的控制标记

-------------------------------经典用法1---------------------------------------------------------
正则表达式				对应字符串
P(Y|YT|YTH|YTHO)?N	    'PN'、'PYN'、'PYTN'、'PYTHN'、'PYTHON'
PYTHON+					'PYTHON'、'PYTHONN'、'PYTHONNN' …
PY[TH]ON				'PYTON'、'PYHON'
PY[^TH]?ON				'PYON'、'PYaON'、'PYbON'、'PYcON'…
PY{:3}N					'PN'、'PYN'、'PYYN'、'PYYYN'
-------------------------------经典用法2---------------------------------------------------------
^[A-Za-z]+$				#由26个字母组成的字符串
^[A-Za-z0-9]+$				#由26个字母和数字组成的字符串
^-?\d+$					#整数形式的字符串
^[0-9]*[1-9][0-9]*$			#正整数形式的字符串
[1-9]\d{5}				#中国境内邮政编码，6位
[\u4e00-\u9fa5]			        #匹配中文字符
\d{3}‐\d{8}|\d{4}‐\d{7}	        #国内电话号码，010-68913536

精确写法
0‐99： [1‐9]?\d
100‐199: 1\d{2}
200‐249: 2[0‐4]\d
250‐255: 25[0‐5]
'''


class CHelper_re(object):
    def __init__(self): 
        pass 
    #匹配字符串的位置
    def test1(self):
        print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配  结果： (0, 3)  第0位开始，长度是3  
        print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配 结果：None
        return "null"
    #search 简单用法
    def test2(self):
        rst = re.search(r'[1‐9]\d{5}', 'BIT 100081')
        print(rst)
        return "null"
    #re.findall() 简单用法
    def test3(self):
        rst = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084') #['100081', '100084']
        print(rst)
        return "null"
    #re.split() 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型。
    def test4(self): 
        rst = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')#['BIT', ' TSU', '']
        rst = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)#['BIT', ' TSU100084']    maxsplit表示最大分割数
        print(rst)
        return "null"
    #re.split() 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型。
    def test5(self): 
        for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
            if m:
                print(m.group(0))    #100081   100084
        return "null"

