#!/usr/bin/env python3
# from typing import *



# def solve(N: int, X: List[int]) -> float:
def solve(N, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = [None for _ in range(5 * N)]
    for i in range(5 * N):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X)
    print(a)

if __name__ == '__main__':
    main()
