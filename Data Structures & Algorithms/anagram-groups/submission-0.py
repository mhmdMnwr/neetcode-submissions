class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for  i in range(len(strs)):
            counter_key = tuple(sorted(Counter(strs[i]).items()))
            seen[counter_key].append(strs[i])
         

        return list(seen.values() )   