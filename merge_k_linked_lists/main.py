class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        cur = self
        res = ''
        while True:
            res += f"{cur.val}"
            if cur.next is None:
                break
            res += " --> "
            cur = cur.next
        return  res


def build_linked_list(arr):
    """ Build a linked list from an array. """
    first = ListNode(arr[0])
    cur = first
    for num in arr[1:]:
        next = ListNode(num)
        cur.next = next
        cur = next

    return first


def binary_insert(node_arr, node):
    """ Insert a value into a sorted array and keep the sort. """
    left, right = 0, len(node_arr)
    mid = (left + right) // 2
    while left < right:
        if node_arr[mid].val < node.val:
            left = mid + 1
        else:
            right = mid
        mid = (left + right) // 2

    node_arr.insert(mid, node)


class Solution:
    def mergeKLists(self, lists):
        lists = [node for node in lists if node is not None]
        if len(lists) == 0:
            return None
        lists = sorted(lists, key=lambda node: node.val)
        first = lists.pop(0)
        if first.next is not None:
            binary_insert(lists, first.next)
        cur = first
        while len(lists) != 0:
            minnode = lists.pop(0)
            cur.next = minnode
            cur = minnode
            if cur.next is not None:
                binary_insert(lists, cur.next)

        return first


if __name__ == '__main__':
    sol = Solution()
    lists = [build_linked_list(arr) for arr in [[1,4,5],[1,3,4],[2,6]]]
    print(sol.mergeKLists(lists))

