#!/usr/bin/env python3
# from typing import *



# def solve(D: int, G: int, p: List[int], c: List[int]) -> int:
def solve(D, G, p, c):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    D, G = map(int, input().split())
    p = [None for _ in range(D)]
    c = [None for _ in range(D)]
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    a = solve(D, G, p, c)
    print(a)

if __name__ == '__main__':
    main()
