import sys
print("你传入的参数是：", sys.argv)
if len(sys.argv) > 1:
    print("你要分析的网址是：", sys.argv[1])
else:
    print("你没有传入网址")
