class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch.isdigit():
                continue
            elif ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            else:
                # Contains invalid character like $, @, #
                return False

        return has_vowel and has_consonant
