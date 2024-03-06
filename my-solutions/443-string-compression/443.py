class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        i = 0
        start = 0

        while i < len(chars):
            if i == 0:
                i += 1
                continue
            elif chars[i] == chars[i - 1]:
                count += 1
                i += 1
                if i == len(chars):
                    char = chars[i - 1]
                    if count > 0:
                        for _ in range(count):
                            chars.pop(start)
                        chars[start] = chars[start] + str(count+1)
            elif chars[i] != chars[i - 1]:
                char = chars[i - 1]
                if count > 0:
                    for _ in range(count):
                        chars.pop(start)
                    chars[start] = chars[start] + str(count+1)
                start += 1
                i = start + 1
                count = 0   

        i = 0
        length = len(chars)
        while i < length:
            chars.extend(list(chars.pop(0)))
            i += 1
        return len(chars)
