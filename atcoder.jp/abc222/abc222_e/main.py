#!/usr/bin/env python3
# from typing import *

MOD = 998244353

# def solve(N: int, M: int, K: int, A: List[int], U: List[int], V: List[int]) -> int:
def solve(N, M, K, A, U, V):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(M)]
    U = [None for _ in range(N - 1)]
    V = [None for _ in range(N - 1)]
    for i in range(M):
        A[i] = int(next(tokens))
    for i in range(N - 1):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, K, A, U, V)
    print(a)

if __name__ == '__main__':
    main()
