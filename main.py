import sys
from addition import add


sys_argv = sys.argv[1:]
print(sys_argv)

op, a, b = sys_argv

a, b = int(a), int(b)

op_function = lambda a, b: a



if op == 'add':
    print("affect add")
    op_function = add


print(op)
print(type(op))


print("result = " , op_function(a,b))

