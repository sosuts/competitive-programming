#!/usr/bin/env python3
# from typing import *


# def solve(N: int, W: int, w: List[int], v: List[int]) -> int:
def solve(N, W, w, v):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, W = map(int, input().split())
    w = [None for _ in range(N)]
    v = [None for _ in range(N)]
    for i in range(N):
        w[i], v[i] = map(int, input().split())
    a = solve(N, W, w, v)
    print(a)


if __name__ == "__main__":
    main()
