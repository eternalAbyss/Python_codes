from . import ListNode, Solution


def test_solution():
    Sol = Solution()
    cur = list1 = ListNode()
    for element in [1, 2, 4]:
        cur = ListNode(element)
        cur = cur.next
    cur = list2 = ListNode()
    for element in [1, 3, 4]:
        cur = ListNode(element)
        cur = cur.next

    cur = list3 = ListNode()
    for element in [1, 1, 2, 3, 4, 4]:
        cur = ListNode(element)
        cur = cur.next

    is_same = True
    res = Sol.mergeTwoLists(list1, list2)
    while res and list3:
        if res.val != list3.val:
            print("Not equal")
            is_same = False
        res, list3 = res.next, list3.next
    if res != None or list3 != None:
        is_same = False
        print(res, list3)
    assert is_same
