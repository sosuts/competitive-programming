#!/usr/bin/env python3
# from typing import *
import sys
from math import ceil, floor

sys.setrecursionlimit(10**6)


# def solve(N: int) -> int:
def solve(x, memo):
    if x == 1:
        return 0
    if x in memo:
        return memo[x]
    else:
        result = x + solve(x // 2, memo) + solve((x + 1) // 2, memo)
        memo[x] = result
    return result


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    memo = dict()
    memo[0] = memo[1] = 0
    a = solve(N, memo)
    print(int(a))


if __name__ == "__main__":
    main()
