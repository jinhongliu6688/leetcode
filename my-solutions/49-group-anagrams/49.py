class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            map[tuple(sorted(word))].append(word)

        answer = []
        for value in map.values():
            answer.append(value)

        return answer
