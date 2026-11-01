class Solution:
    def containsPattern(self, a: List[int], m: int, k: int) -> bool:
        return bool(search(rf'(.{{{m}}})\1{{{k-1}}}',''.join(map(chr,a))))