from . import Solution

def test_solution():
    Sol = Solution()
    res = Sol.mergeTwoLists([1,2,4], [1,3,4])
    assert res==[1,1,2,3,4,4]