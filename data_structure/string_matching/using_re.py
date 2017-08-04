"""
@description: simple introduce for re module
@author: merleLK
@contact: merle.liukun@gmail.com
@date: 17-8-4
"""
import re

# 原始字符串(raw string) R+ r+
print(r"C:\course" == "C:\\course")
print(R"hello")

# re module keyword : . ^ $ * + ? \ | { } [ ] ( )   14

r1 = re.compile("abc")

"""
    字符组
    [...] 匹配括号内的任一个字符
    [0-9] 顺序列出  匹配所有十进制数
    [0-9a-zA-Z] 匹配所有字母和数字
    
    ^ 求补集
    [^0-9] 匹配所有非十进制数的字符
    [^ \t\v\n\f\r] 匹配所有非空白字符
    
    ..  匹配任意字符
    a..b 匹配任意a开头b结尾的四字符串
    a[1-9][1-9] 可以匹配 a10, a11...a99
    
    常用字符组
    \d  ===  [0-9]
    \D  ===  [^0-9]
    \s  ===  [\t\v\n\f\r]
    \S  ===  [^ \t\v\n\f\r]
    \w  ===  [0-9a-zA-Z]
    \W  ===  [^ 0-9a-zA-Z]
    
    p\w\w\w  : p开头后边跟着三个字母数字字符 匹配
    
    repeat:
        * 模式部分一次或者人一次重复   a* a的0次或者任意多次出现
        re.split('[ ,]*', s)  # 把串s按空格和逗号（任意个）切分
        re.split('[ ,]*', '1  2,      3, 4   ,5')
        
        + : 表示1次或者多次重复
        \d+ === \d\d*
        {n} 可以确定重复的次数  a{n} 与a匹配的串的n次重复匹配
        '(010-)?[2-9][0-9]{7}'  可表示北京固话号码
        
        对于 *, ?, {n} 作用于最小的表达式
        ()可以的圈住范围
        
        ? : 表示0次或者1次重复
        -?\d+  表示整数的字符串
        
        重复范围
        {m,n}
        a{3, 7}  与3到7个a构成的串匹配
        m,n 都可以省略
        
        -- * + ? {m,n} 都采取贪婪匹配策略，与被匹配串中最长的合适子串匹
        配（因为它们可能出现更大的模式里，要照顾上下文的需要）
        
        --- *? +? ?? {m,n}?（各运算符后增加一个问号）的语义与上面几
        个运算符分别对应，但采用非贪婪匹配（最小匹配）的策略
        
        选择运算符  | 或者
        匹配国内固定电话号码：'0\d{2}-\d{8}|0\d{3}-\d{7,8}'
        
        行首匹配： 以^开头的模式，只能与一行的前缀字符串匹配
        re.search('^for', 'book for re')  
        get None;
        
        行尾匹配 : 以$符号结尾的模式 只与一行的后缀匹配
        re.search('fish$', 'eat fishes')
        get None
        
        串首匹配：
        \A 开头的模式只与被匹配字符串的前缀匹配
        
        串尾匹配：
        \Z 开头的模式只与被匹配字符串的后缀匹配
        
        单词边界
        \b 描述单词边界  表示单词边界匹配一个字符串。
            单词是字母数字的连续序列， 边界就是非字母数字字符或者无字符（串的开头或者结束）
        Tips: Python的字符串中\b 表示退格符， 与re中混淆
            可以：
            1.将 \ 双写  表示把\本身发送给re.compile 如'\\b123\\b'
            2.使用Python原始字符串， 其中的\没有转义， 上边的可以写为  r'\b123\b'
        给个实例 
            匹配Python整数的模式  
             '\\b(0+|[1-9]\d*)\\b'
             r'\b(0+|[1-9]\d*)\b'
            考虑有+-号的整数
                '[+-]?\\b(0+|[1-9]\d+)\\b'
                其匹配 x+5 中的+5  但不匹配3 +- 5 中的-5
                
                
        边界
        \B 是 \b的补集 也是匹配空串， 但要求相应位置是字母或者数字
            实例:
            re.findall('py.\B', 'Python, py2, py342, py1py2py4')
        
"""


# 求一个Python程序中出现的所有整数之和
def sum_int(filename):
    re_int = r'\b(0+|[1-9]\d+)\b'
    inf = open(filename)
    if inf is None:
        inf = 0
    i_list = map(int, re.findall(re_int, inf.read()))
    s = 0
    for n in i_list:
        s += n
    return s


if __name__ == '__main__':
    my_string = "aaaabcasdfasfasgfasgdsghdfjkaF"

    print(re.search(r1, my_string))  # 寻找子串
    print(re.match(r1, my_string))  # 匹配前缀
    print(re.split(r1, my_string))  # 按照pattern分割字符串
    print(re.findall(r1, my_string))
    # print(re.split('[ ,]*', '1  2,      3, 4   ,5'))
    # print(re.split('a*', 'abbaaabbdbbabbababbabb'))
    print(re.match('ab*', 'abbbbbbbbbbbbc'))
    print(re.search('^for', 'book for re'))
    print(re.search('^book', 'book for re').group())
    print(re.search('fish$', 'eat fishes'))
    print(re.search('fish$', 'eat fish'))
    file = 'str_matching.py'
    print(sum_int(file))
