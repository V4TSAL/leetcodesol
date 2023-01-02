class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        else:
            if word.islower() or word.isupper():
                return True
            else:
                if word[0].islower():
                    return False
                else:
                    for i in word[1:]:
                        if i.isupper():
                            return False
                    return True
                        