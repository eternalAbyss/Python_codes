from . import Solution


def test_solution():
    Sol = Solution()
    res = Sol.longestCommonPrefix(["flower", "flow", "flight"])
    assert res == "fl"
