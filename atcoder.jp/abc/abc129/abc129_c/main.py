#!/usr/bin/env python3
# from typing import *

MOD = 1000000007


# def solve(k: int, n: int, a: List[int]) -> int:
def solve(k, n, a):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    k, n = map(int, input().split())
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = int(input())
    a1 = solve(k, n, a)
    print(a1)


if __name__ == "__main__":
    main()