#!/usr/bin/env python3
# from typing import *



# def solve(N: int, Q: int, a: List[int], x: List[int], k: List[int]) -> Tuple[str, List[str]]:
def solve(N, Q, a, x, k):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    Q = int(next(tokens))
    a = [None for _ in range(N)]
    x = [None for _ in range(Q)]
    k = [None for _ in range(Q)]
    for i in range(N):
        a[i] = int(next(tokens))
    for i in range(Q):
        x[i] = int(next(tokens))
        k[i] = int(next(tokens))
    assert next(tokens, None) is None
    c, e = solve(N, Q, a, x, k)
    print(c)
    for i in range(Q):
        print(e[i])

if __name__ == '__main__':
    main()
