class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())'''

        anagrams = {}
        for i in strs:
            sorted_arr = "".join(sorted(i))
            
            if sorted_arr in anagrams:
                anagrams[sorted_arr].append(i)
            
            else: 
                anagrams[sorted_arr] = [i]

        return list(anagrams.values())