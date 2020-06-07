# -*- coding: utf-8 -*-
# @Time    :  2020/6/7 2:38
# @Author  : nice0e3
# @FileName: exe test.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/nice0e3/

# -*- coding: utf-8 -*-
# @Time    :  2020/6/7 1:55
# @Author  : nice0e3
# @FileName: exe2shellcode.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/nice0e3/
import sys

def exe2shellcode(exe):
    shellcode =''
    with open(exe,'rb')as f:
        f = f.read()
        for i in f:
            if i == 0:
                pass
            else:

                if len(str(i)) == 1:
                    shellcode += '\\x' + '0'+hex(i)[2:]

                elif i == 10:
                    shellcode += '\\x' + '0' + hex(i)[2:]
                elif i == 11:
                    shellcode += '\\x' + '0' + hex(i)[2:]
                elif i == 12:
                    shellcode += '\\x' + '0' + hex(i)[2:]
                elif i == 13:
                    shellcode += '\\x' + '0' + hex(i)[2:]
                elif i == 14:
                    shellcode += '\\x' + '0' + hex(i)[2:]
                elif i == 15:
                    shellcode += '\\x' + '0' + hex(i)[2:]



                else:
                    shellcode += '\\x' + hex(i)[2:]

                # shellcode += '\\x' + hex(i)[2:]
    return (shellcode)



def main():
    exe = sys.argv[1]
    shellcode = exe2shellcode(exe)
    print(shellcode)
    with open('shellcode.txt','a')as file:
        file.write(shellcode)
if __name__ == '__main__':
    main()




