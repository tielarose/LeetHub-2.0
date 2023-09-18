from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # this function ensures all letters in s not in order appear at the end of the string; not necessary per the problem, but I wanted a consistent result
        def default_val():
            return len(order) + 1

        sort_order = defaultdict(default_val)

        for ind, char in enumerate(order):
            sort_order[char] = ind

        s_arr = list(s)

        s_arr.sort(key=lambda x: sort_order[x])

        return ''.join(s_arr)