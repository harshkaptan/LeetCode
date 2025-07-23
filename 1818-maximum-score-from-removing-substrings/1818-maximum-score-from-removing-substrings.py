class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, points):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(c)
            return "".join(stack), score

        if x >= y:
            first_pat, second_pat = ('a', 'b', x), ('b', 'a', y)
        else:
            first_pat, second_pat = ('b', 'a', y), ('a', 'b', x)

        t, points1 = remove_substring(s, *first_pat)
        _, points2 = remove_substring(t, *second_pat)

        return points1 + points2
