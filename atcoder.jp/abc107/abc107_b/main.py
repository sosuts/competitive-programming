#!/usr/bin/env python3
# from typing import *



# def solve(H: str, W: str, a: List[List[str]]) -> Any:
def solve(H, W, a):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    H = next(tokens)
    W = next(tokens)
    a = [[None for _ in range(W)] for _ in range(H)]
    for j in range(H):
        for i in range(W):
            a[j][i] = next(tokens)
    assert next(tokens, None) is None
    ans = solve(H, W, a)
    print(ans)  # TODO: edit here

if __name__ == '__main__':
    main()
