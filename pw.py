#! python3
# pw.py 口令保管箱

import pyperclip
import sys


PASSWORDS = {'zhangyixing': '19990720',
             'zhoujun': '19990715',
             'zouyiheng': '1122334455',
             'zhuhaojiang': '8888888'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account429] - 复制用户密码')
    sys.exit()

# 获取命令参数
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
