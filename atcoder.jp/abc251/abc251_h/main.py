#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, K: int, a: List[int], c: List[int]) -> List[List[str]]:
def solve(N, M, K, a, c):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, K = map(int, input().split())
    a = [None for _ in range(M)]
    c = [None for _ in range(M)]
    for i in range(M):
        a[i], c[i] = map(int, input().split())
    B = solve(N, M, K, a, c)
    print(*[B[i][i] for i in range(K)])

if __name__ == '__main__':
    main()
