def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """

    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        """
        Expand around a given center and return the start and end indices
        (inclusive) of the longest palindrome found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # We stop when the characters don't match, so step back in one position
        # left + 1 and right - 1 are the valid palindrome bounds
        return left + 1, right - 1

    start = 0
    end = 0

    for i in range(len(s)):
        # Odd-length palindrome (center at i)
        left1, right1 = expand_around_center(i, i)
        # Even-length palindrome (center between i and i + 1)
        left2, right2 = expand_around_center(i, i + 1)

        # Choose the longer of the two
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start : end + 1]
