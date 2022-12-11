from typing import Optional, List


class newNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[newNode]) -> List[Optional[newNode]]:
        res = []
        hmap = {}

        def recurse(node, path):
            if node is None:
                return '#'

            path += ','.join([str(node.val), recurse(node.left, path), recurse(node.right, path)])

            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
            print(path)
            print(hmap)
            return path

        recurse(root, '')
        return res

if __name__ == '__main__':
    root = None
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(2)
    root.right.left.left = newNode(4)
    root.right.right = newNode(4)
    s = Solution()
    print(s.findDuplicateSubtrees(root))
