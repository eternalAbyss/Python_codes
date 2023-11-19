from . import Solution

def test_solution():
    Sol = Solution()
    res = Sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    assert res == 5