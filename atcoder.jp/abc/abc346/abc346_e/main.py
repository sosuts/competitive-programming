#!/usr/bin/env python3
# from typing import *



# def solve(H: int, W: int, M: int, T: List[int], A: List[int], X: List[int]) -> Tuple[int, List[int], List[int]]:
def solve(H, W, M, T, A, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W, M = map(int, input().split())
    T = [None for _ in range(M)]
    A = [None for _ in range(M)]
    X = [None for _ in range(M)]
    for i in range(M):
        T[i], A[i], X[i] = map(int, input().split())
    n, a, b = solve(H, W, M, T, A, X)
    print(n)
    for i in range(n):
        print(a[i], b[i])

if __name__ == '__main__':
    main()
