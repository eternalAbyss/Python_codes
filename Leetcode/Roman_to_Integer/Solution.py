class Solution:
    def romanToInt(self, s: str) -> int:
        rom_num_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num_list = list(s)
        final_num = 0
        for index, num in enumerate(num_list):
            if index == len(num_list) - 1:
                final_num += rom_num_map[num]
            elif num == 'I' and (num_list[index+1]=='V' or num_list[index+1]=='X'):
                    final_num -= 1
            elif num == 'X' and (num_list[index+1]=='L' or num_list[index+1]=='C'):
                    final_num -= 10
            elif num == 'C' and (num_list[index+1]=='D' or num_list[index+1]=='M'):
                    final_num -= 100
            else:        
                final_num += rom_num_map[num]
        return final_num