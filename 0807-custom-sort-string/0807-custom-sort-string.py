from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_s = Counter(s)
        result = []

        for char in order:
            result.append(char * count_s[char])
            count_s[char] = 0

        for char in count_s:
            result.append(char * count_s[char])

        return ''.join(result)