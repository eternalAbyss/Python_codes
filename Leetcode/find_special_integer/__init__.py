class Solution:

    def findSpecialInteger(self, arr: list[int]) -> int:
        arr_len = len(arr)
        # check if the array is just one number long
        if arr_len == 1:
            # returning the first number
            return arr[0]
        else:
            # Base logic
            num_dict = dict()
            in_nums = list(dict.fromkeys(arr))
            # Check if there are more than one unique numbers
            if len(in_nums) == 1:
                # Returning the only number since it will be unique
                return in_nums[0]

            # Check if the array has more than one number
            elif len(in_nums) > 1:
                num_dict[in_nums[0]] = arr.index(in_nums[1])
                # Looping through the further numbers to make the final dictionary
                for i in range(1, len(in_nums)):
                    if i == len(in_nums) - 1:
                        num_dict[in_nums[i]] = len(arr) - (arr.index(
                            in_nums[i]))
                        print(len(arr) - (arr.index(in_nums[i]) - 1))
                    else:
                        num_dict[in_nums[i]] = arr.index(
                            in_nums[i + 1]) - arr.index(in_nums[i])
                print(num_dict)
        return max(zip(num_dict.values(), num_dict.keys()))[1]
