#!/usr/bin/env python3
# from typing import *


# def solve(H: str, W: str, S: List[List[str]]) -> Tuple[int, int]:
def solve(H, W, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    H = next(tokens)
    W = next(tokens)
    S = [[None for _ in range(H + W + 4)] for _ in range(H + W + 4)]
    for j in range(H + 4):
        for i in range(W):
            S[i + j][i + j] = next(tokens)
    assert next(tokens, None) is None
    a, b = solve(H, W, S)
    print(a, b)


if __name__ == "__main__":
    main()