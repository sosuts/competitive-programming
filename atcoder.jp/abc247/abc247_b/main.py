#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(N: int, s: List[str], t: List[str]) -> str:
def solve(N, s, t):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    s = [None for _ in range(N)]
    t = [None for _ in range(N)]
    for i in range(N):
        s[i], t[i] = input().split()
    a = solve(N, s, t)
    print(a)

if __name__ == '__main__':
    main()
