#!/usr/bin/env python3
# from typing import *

MOD = 998244353

# def solve(N: int, p: List[int], q: List[int]) -> List[str]:
def solve(N, p, q):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    p = [None for _ in range(N - 1)]
    q = [None for _ in range(N - 1)]
    for i in range(N - 1):
        p[i], q[i] = map(int, input().split())
    E = solve(N, p, q)
    print(*[E[i] for i in range(N)])

if __name__ == '__main__':
    main()
