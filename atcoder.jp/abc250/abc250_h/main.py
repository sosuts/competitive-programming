#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(N: int, M: int, K: int, a: List[int], b: List[int], c: List[int], Q: int, x: List[int], y: List[int], t: List[int]) -> List[str]:
def solve(N, M, K, a, b, c, Q, x, y, t):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, K = map(int, input().split())
    a = [None for _ in range(M)]
    b = [None for _ in range(M)]
    c = [None for _ in range(M)]
    for i in range(M):
        a[i], b[i], c[i] = map(int, input().split())
    Q = int(input())
    x = [None for _ in range(Q)]
    y = [None for _ in range(Q)]
    t = [None for _ in range(Q)]
    for i in range(Q):
        x[i], y[i], t[i] = map(int, input().split())
    d = solve(N, M, K, a, b, c, Q, x, y, t)
    for i in range(K):
        print(d[i])

if __name__ == '__main__':
    main()
