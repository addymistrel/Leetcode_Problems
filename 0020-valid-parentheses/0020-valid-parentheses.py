class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{',']':'['}
        tmp = []
        for k in s:
            if k=='(' or k=='{' or k=='[':
                tmp.append(k)
            elif len(tmp)==0:
                tmp.append(k)
            else:
                p = tmp.pop()
                if p!=d[k]:
                    return False
        return False if len(tmp)>0 else True

        