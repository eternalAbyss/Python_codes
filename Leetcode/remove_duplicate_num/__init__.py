from time import sleep


class Solution:
    def __init__(self):
        self.len_counter = 0

    def removeDuplicates(self, nums: list[int]) -> int:
        def swap(num_list: list, index1: int):
            num_list.append(num_list.pop(index1))
            return num_list

        def moving_duplicates(self, num_list):
            prev = "placeholder"
            max_number = max(num_list)
            for index in range(len(num_list) - 1):
                if index == len(num_list) - 1:
                    break
                if num_list[index] == prev:
                    i = index
                    while num_list[i] == prev:
                        if num_list[i] == max_number:
                            break
                        num_list = swap(num_list, index)
                    prev = num_list[index]
                else:
                    prev = num_list[index]
                if max_number == num_list[index]:
                    self.len_counter = index + 1
                    break

        moving_duplicates(self, nums)
        num_len = nums.index(max(nums)) + 1
        return num_len
