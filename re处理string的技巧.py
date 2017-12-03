# re模块的split（）方法可以分割多个字符串
import re
i = 'a b,c;d:n'
res = re.split(r'[,;:\s]\s*', i)
print(res)

# re模块的sub方法可以代替replace解决复杂替换问题。
res = re.sub(r'(a)', r'\y', i)  # 第一个参数是匹配组，第二个是替换组，第三个是字符串。
print(res)

# 删除不需要的字符 strip()
s = ' -yyyy '
s1 = s.strip()
s2 = s.lstrip()
s3 = s.rstrip()
s4 = s.strip(' ,')
print(s + '\n', s1 + '\n', s2 + '\n', s3 + '\n', s4 + '\n')

# 合并一个list中的字符串。

l = ['a', 'b', 'c']
s1 = ''.join(l)
s2 = ','.join(l)
print(s1 + '\n', s2 + '\n')
