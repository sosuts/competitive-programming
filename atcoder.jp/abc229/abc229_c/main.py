#!/usr/bin/env python3
# from typing import *



# def solve(N: int, W: int, A: List[int], B: List[int]) -> int:
def solve(N, W, A, B):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, W = map(int, input().split())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    a = solve(N, W, A, B)
    print(a)

if __name__ == '__main__':
    main()
