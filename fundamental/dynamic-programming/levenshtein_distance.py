def levenshtein(s1, s2):
    """
    >>> levenshtein('kitten', 'sitting')
    3
    >>> levenshtein('あいうえお', 'あいうえお')
    0
    >>> levenshtein('あいうえお', 'かきくけこ')
    5
    """
    l1, l2 = len(s1), len(s2)

    dp = [[0] * (l2 + 1) for i1 in range(l1 + 1)]

    for i1 in range(l1 + 1):
        dp[i1][0] = i1

    for i2 in range(l2 + 1):
        dp[0][i2] = i2

    for i1 in range(1, l1 + 1):
        for i2 in range(1, l2 + 1):
            cost = 0 if s1[i1 - 1] == s2[i2 - 1] else 1
            dp[i1][i2] = min(dp[i1 - 1][i2] + 1, dp[i1][i2 - 1] + 1, dp[i1 - 1][i2 - 1] + cost)

    return dp[l1][l2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
