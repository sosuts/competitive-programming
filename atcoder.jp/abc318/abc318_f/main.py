#!/usr/bin/env python3
# from typing import *



# def solve(N: int, X: List[int], L: List[int]) -> int:
def solve(N, X, L):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = [None for _ in range(N)]
    L = [None for _ in range(N)]
    for i in range(N):
        X[i] = int(next(tokens))
    for i in range(N):
        L[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X, L)
    print(a)

if __name__ == '__main__':
    main()
