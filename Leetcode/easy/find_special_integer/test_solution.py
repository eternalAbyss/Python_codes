from . import Solution


def test_solution():
    Sol = Solution()
    res = Sol.findSpecialInteger([6700,8858,8858,8858,8858])
    assert res == 8858
