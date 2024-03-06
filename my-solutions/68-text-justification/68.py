class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line_length = 0
        line = []
        result = []
        i = 0
        num_words = len(words)

        while i < num_words:
            word = words[i]
            if line_length + len(word) == maxWidth:
                line.append(word)
                result.append("".join(line))
                line = []
                line_length = 0
                i += 1
                continue
            elif line_length + len(word) > maxWidth:
                line.pop()
                line_length -= 1
                if " " not in line:
                    line.append(" " * (maxWidth - len("".join(line))))
                else:
                    while line_length < maxWidth:
                        for x, _ in enumerate(line):
                            if " " in line[x]:
                                line[x] += " "
                                line_length += 1
                            if line_length == maxWidth:
                                break
                result.append("".join(line))
                line = []
                line_length = 0

            line_length += len(word) + 1
            line.append(word)
            line.append(" ")
            i += 1

        if line != []:
            if line_length - 1 == maxWidth:
                line.pop()
                result.append("".join(line))
            else:
                result.append("".join(line) + " " * (maxWidth - len("".join(line))))

        return result
