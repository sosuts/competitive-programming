#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, X: List[int], Y: List[int], P: List[int], Q: List[int]) -> float:
def solve(N, M, X, Y, P, Q):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    P = [None for _ in range(M)]
    Q = [None for _ in range(M)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    for i in range(M):
        P[i], Q[i] = map(int, input().split())
    a = solve(N, M, X, Y, P, Q)
    print(a)

if __name__ == '__main__':
    main()
