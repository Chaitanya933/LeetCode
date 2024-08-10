class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        prefix_length=len(prefix)
        for i in strs[1:]:
            while prefix!=i[0:prefix_length]:
                prefix_length-=1
                if prefix_length==0:
                    return ""
                prefix=prefix[0:prefix_length]
        return prefix