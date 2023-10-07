class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = ''
        b = []
        for i in range(len(haystack)):
            if i <= len(haystack) - len(needle):
                for j in range(i,len(needle)+i):
                    result += haystack[j]
                b.append(result)
                result = ''
        for i in range(len(b)):
            print(b[i])
            if b[i] == needle:               
                return i
                break
        return -1
    

                # or


        try:
            x = haystack.index(needle)
            return x
        except:
            return -1