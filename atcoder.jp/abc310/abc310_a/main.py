#!/usr/bin/env python3
# from typing import *



# def solve(N: int, P: int, Q: int, D: List[int]) -> int:
def solve(N, P, Q, D):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = int(next(tokens))
    Q = int(next(tokens))
    D = [None for _ in range(N)]
    for i in range(N):
        D[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, P, Q, D)
    print(a)

if __name__ == '__main__':
    main()