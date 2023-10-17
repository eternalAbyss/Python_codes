class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0 :
            return ""
        prefix_list = list()
        strs_len = [len(item) for item in strs]
        shortest_string = min(strs_len) 
        if shortest_string == 0:
            return ""
        prefix = strs[0][0]
        flag = False
        for i in range(shortest_string):
            for item in strs:
                if item[i] != prefix:
                    flag = True
            if flag:
                return ''.join(prefix_list)
            prefix_list.append(strs[0][i])
            if i < (shortest_string - 1):
                prefix = strs[0][i+1]
            else:
                return ''.join(prefix_list)