#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, A: List[int], B: List[int]) -> Tuple[str, List[str]]:
def solve(N, M, A, B):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K, v = solve(N, M, A, B)
    print(K)
    for i in range(K):
        print(v[i])

if __name__ == '__main__':
    main()
