#!/usr/bin/env python3
# from typing import *
from collections import OrderedDict


# def solve(S: int, K: int) -> int:
def solve_WC(S, K):
    """
    (n-1)日後にはそれぞれの数字n-1が(n-1)個増える
    10日後には9が増える

    1回目. 0123456789
    2回目. 0123456789
    3回目. 0123456789

    増え方は例えば3だと、1, 3, 9,...だからnum*n^n
    N = 5000兆 = 5*10^15
    2がN//10回増えたとすると、log10(2^(5*10**15))でだいたい15桁くらいになる？
    10^18桁の数はメモリに乗らないから、S[i]の長さを追跡することはできないはず。つまりK番目までの数は記憶できない。
    長さがK以上になったらK番目の数は変化しない。
    log10(3^24) = 11.4504なので、3^24 = 10^11.4504...。
    10^11 <= 3^23 < 10^12より、3^23は12桁の数。
    この問題では、数^5*10**15なので、どの数も10**18個以上になる
    """
    N = 10**12 * 5000
    loop = (N - 1) // 10
    # mod = (N) % 10
    # print(loop, mod)
    left = 0
    right = 1
    for i in range(len(S)):
        print(right)
        if int(S[i]) != 1:
            right = int(S[i]) ** loop
        if K <= right:
            return S[i]
        else:
            left = right


def solve(S, K):
    for i in range(K):
        if int(S[i]) != 1:
            return S[i]
    return 1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    K = int(input())
    a = solve(S, K)
    print(a)


if __name__ == "__main__":
    main()
