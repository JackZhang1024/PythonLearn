# -*- coding:utf-8 -*-
from io import StringIO
from io import BytesIO
#想内存中写入一句话
str=StringIO()
str.write('This is a test')
print(str.getvalue())

f=StringIO('uuuuuuuuuuuuuuuuuuuuuuuuuuu\nooooooooooooooooooo\npppppppppppppppp')
while True:
    s=f.readline()
    if s == '':
       break
    print(s.strip())
f2=BytesIO()
f2.write('中国'.encode('utf-8'))
print(f2.getvalue())
f3=BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
print(f3.read())
