#!/usr/bin/env python3


from re import A


def main():
    for i in range(1, 11):
        tri = triple(i)
        sq = square(i)
        if tri < sq:
            break
        print(f"triple({i})=={tri} square({i})=={sq}")

def triple(a):
    return a*3

def square(a):
    return a*a

if __name__ == "__main__":
    main()
