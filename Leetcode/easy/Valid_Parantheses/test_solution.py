from . import Solution


def test_solution():
    Sol = Solution()
    res = Sol.isValid("(}")
    assert res == False
