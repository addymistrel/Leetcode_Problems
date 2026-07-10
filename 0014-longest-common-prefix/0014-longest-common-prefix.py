class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        ind = 0
        for k in strs[0]:
            isPresentInAll = True
            for i in range(1, len(strs)):
                if ind >= len(strs[i]):
                    isPresentInAll = False
                    break
                if strs[i][ind] != k:
                    isPresentInAll = False
                    break
            if not isPresentInAll:
                break
            lcp += k
            ind += 1
        return lcp