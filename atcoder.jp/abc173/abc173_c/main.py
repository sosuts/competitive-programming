#!/usr/bin/env python3
# from typing import *



# def solve(H: str, W: str, K: str, c: List[List[str]]) -> int:
def solve(H, W, K, c):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    H = next(tokens)
    W = next(tokens)
    K = next(tokens)
    c = [[None for _ in range(H + W + 4)] for _ in range(H + W + 4)]
    for j in range(H + 4):
        for i in range(W):
            c[i + j][i + j] = next(tokens)
    assert next(tokens, None) is None
    a = solve(H, W, K, c)
    print(a)

if __name__ == '__main__':
    main()
