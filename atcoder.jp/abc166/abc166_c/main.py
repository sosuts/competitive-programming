#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, H: List[int], A: List[int], B: List[int]) -> int:
def solve(N, M, H, A, B):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    H = [None for _ in range(N)]
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(N):
        H[i] = int(next(tokens))
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, H, A, B)
    print(a)

if __name__ == '__main__':
    main()
