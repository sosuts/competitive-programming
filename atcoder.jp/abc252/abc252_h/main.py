#!/usr/bin/env python3
# from typing import *



# def solve(N: int, C: int, K: int, D: List[int], V: List[int]) -> int:
def solve(N, C, K, D, V):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, C, K = map(int, input().split())
    D = [None for _ in range(N)]
    V = [None for _ in range(N)]
    for i in range(N):
        D[i], V[i] = map(int, input().split())
    a = solve(N, C, K, D, V)
    print(a)

if __name__ == '__main__':
    main()
