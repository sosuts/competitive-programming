#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(N: str, S: List[List[str]], T: List[List[str]]) -> str:
def solve(N, S, T):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = next(tokens)
    S = [[None for _ in range(N)] for _ in range(2 * N + 2)]
    T = [[None for _ in range(N)] for _ in range(2 * N + 2)]
    for j in range(N + 2):
        for i in range(N):
            S[i + j][i] = next(tokens)
    for j in range(N + 2):
        for i in range(N):
            T[i + j][i] = next(tokens)
    assert next(tokens, None) is None
    a = solve(N, S, T)
    print(a)

if __name__ == '__main__':
    main()
