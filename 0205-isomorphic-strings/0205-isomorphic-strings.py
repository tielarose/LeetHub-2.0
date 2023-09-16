class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = dict()
        mapped_letters = set()

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in char_map:
                if t_char in mapped_letters:
                    return False
                else:
                    char_map[s_char] = t_char
                    mapped_letters.add(t_char)
            else:
                if char_map[s_char] != t_char:
                    return False

        return True