#!/usr/bin/env python3
# from typing import *



# def solve(a: str, b: int, c: List[int], d: List[List[str]]) -> int:
def solve(a, b, c, d):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = next(tokens)
    b = int(next(tokens))
    c = [None for _ in range(b)]
    d = [[None for _ in range(c_i)] for _ in range(b)]
    for i in range(b):
        c[i] = int(next(tokens))
        for j in range(c_i):
            d[i][j] = next(tokens)
    assert next(tokens, None) is None
    a1 = solve(a, b, c, d)
    print(a1)

if __name__ == '__main__':
    main()
