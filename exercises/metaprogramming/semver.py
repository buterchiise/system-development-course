import sys

v1, v2 = sys.argv[1], sys.argv[2]

def parse(v):
    return tuple(map(int, v.split(".")))

a, b = parse(v1), parse(v2)

if a[0] != b[0]:
    print("MAJOR 变更，可能不兼容")
elif a[1] != b[1]:
    print("MINOR 变更，向后兼容")
else:
    print("PATCH 变更，安全升级")
