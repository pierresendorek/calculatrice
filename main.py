import sys
from addition import add
from division import div

sys_argv = sys.argv[1:]
a, op, b = sys_argv
a, b = int(a), int(b)
op_function = lambda a, b: a

if op == 'add':
    print("affect add")
    op_function = add
elif op == 'div':
    print('affect div')
    op_function = div


print("result = " , op_function(a,b))

