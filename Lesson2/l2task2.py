import sys
import struct
import datetime
import datetime
# sl = [5,6,7,8,9]
# ls=sl[:]
# # ls=sl

# print(struct.calcsize("P"))
# print(sys.getsizeof("P"))
#
# print(sys.float_info)
# print(sys.version)
# print(sys.argv)
# print(dir(42))
# print(hex(id(sl)))
# print(oct(id(sl)))
# print(hex(id(ls)))
# print(oct(id(ls)))
# print(sl is ls)
# print(sl == ls)
# print(id(sl) is id(ls))
# print(id(sl) == id(ls))

def doSmth():
    sl = [5, 6, 7, 8, 9]
    ls = sl[:]
    sl = [5,6,7,8,9]
    ls=sl[:]
    # ls=sl

    # print(struct.calcsize("P"))
    # print(sys.getsizeof("P"))
    #
    # print(sys.float_info)
    # print(sys.version)
    # print(sys.argv)
    # print(dir(42))
    # print(hex(id(sl)))
    # print(oct(id(sl)))
    # print(hex(id(ls)))
    # print(oct(id(ls)))
    print(sl is ls)
    print(sl == ls)
    print(id(sl) is id(ls))
    print(id(sl) == id(ls))

def do_date():
    d = datetime.datetime.now()
    sd = "test passed {}.{} on {}:{}".format(d.day, d.month, d.hour, d.minute)
    print(sd)

print(__name__)
if __name__ == '__main__':
    doSmth()
    do_date()