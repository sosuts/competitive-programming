#!/usr/bin/env python3
# from typing import *



# def solve(N: int, t: List[int], l: List[int], r: List[int]) -> int:
def solve(N, t, l, r):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    t = [None for _ in range(N)]
    l = [None for _ in range(N)]
    r = [None for _ in range(N)]
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())
    a = solve(N, t, l, r)
    print(a)

if __name__ == '__main__':
    main()
