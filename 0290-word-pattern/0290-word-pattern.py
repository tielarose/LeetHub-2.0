from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()

        def default_value():
            return 0

        pattern_to_s_map = defaultdict(default_value)
        s_to_pattern_map = defaultdict(default_value)

        if len(s_arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = s_arr[i]

            if char not in pattern_to_s_map and word not in s_to_pattern_map:
                pattern_to_s_map[char] = word
                s_to_pattern_map[word] = char
            else:
                if pattern_to_s_map[char] != word or s_to_pattern_map[word] != char:
                    return False

        return True