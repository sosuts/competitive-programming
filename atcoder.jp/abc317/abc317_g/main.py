#!/usr/bin/env python3
# from typing import *

YES = 'Yes'

# def solve(N: int, M: int, A: List[List[int]]) -> Tuple[List[str], List[List[str]], str]:
def solve(N, M, A):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [[None for _ in range(M)] for _ in range(N)]
    for j in range(N):
        for i in range(M):
            A[j][i] = int(next(tokens))
    assert next(tokens, None) is None
    c, e, f = solve(N, M, A)
    for i in range(N):
        print(c[i])
        for j in range(i):
            print(e[i][j], end=' ')
    print(f)

if __name__ == '__main__':
    main()
