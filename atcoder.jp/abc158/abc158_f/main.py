#!/usr/bin/env python3
# from typing import *

MOD = 998244353

# def solve(N: int, X: List[int], D: List[int]) -> int:
def solve(N, X, D):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    X = [None for _ in range(N)]
    D = [None for _ in range(N)]
    for i in range(N):
        X[i], D[i] = map(int, input().split())
    a = solve(N, X, D)
    print(a)

if __name__ == '__main__':
    main()
