from . import Solution


def test_solution():
    Sol = Solution()
    res = Sol.romanToInt("III")
    assert res == 3
