#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, u: List[int], v: List[int], W: List[int], A: List[int]) -> int:
def solve(N, M, u, v, W, A):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    u = [None for _ in range(M)]
    v = [None for _ in range(M)]
    W = [None for _ in range(N)]
    A = [None for _ in range(N)]
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    for i in range(N):
        W[i] = int(next(tokens))
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, u, v, W, A)
    print(a)


if __name__ == "__main__":
    main()
