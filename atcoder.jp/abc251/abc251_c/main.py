#!/usr/bin/env python3
# from typing import *



# def solve(N: int, S: List[str], T: List[int]) -> int:
def solve(N, S, T):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    S = [None for _ in range(N)]
    T = [None for _ in range(N)]
    for i in range(N):
        S[i] = next(tokens)
        T[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, S, T)
    print(a)

if __name__ == '__main__':
    main()
