#!/usr/bin/env python3
# from typing import *


# def solve(N: str, S: List[List[str]]) -> str:
def solve(N, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = next(tokens)
    S = [[None for _ in range(2 * N + 4)] for _ in range(2 * N + 4)]
    for j in range(N + 4):
        for i in range(N):
            S[i + j][i + j] = next(tokens)
    assert next(tokens, None) is None
    a = solve(N, S)
    print(a)


if __name__ == "__main__":
    main()