#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    z = 0
    count = len(sys.argv)
    for i in range(1, count):
        z = z + int(sys.argv[i])
    print("{}".format(z))
