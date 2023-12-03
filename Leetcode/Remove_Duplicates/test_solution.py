from . import Solution

def test_solution():
    Sol = Solution()
    res = Sol.removeElement([3,2,2,3],3)
    assert res == 2