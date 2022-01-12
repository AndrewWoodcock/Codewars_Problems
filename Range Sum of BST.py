


graph = {10: [5, 15],
         5: [3, 7],
         15: [None, 18]}

low = 7
high = 15


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans


graph_list = [10, 5, 15, 3, 7, None, 18]


def build_graph(g_lis: list) -> dict:
    out_graph = {}
    # init root node
    root = g_lis.pop(0)
    out_graph[root] = []
    j = 0
    parent = root
    for i in range(0, len(g_lis)):
        if j < 2:
            child = g_lis.pop(0)
            out_graph[parent].append(child)
            j += 1
        elif j >= 2:
            parent



    print(out_graph)



def main():

    build_graph(graph_list)

    xsum = 0
    for key, value in graph.items():
        parent = TreeNode(key, value[0], value[1])
        solution = Solution


if __name__ == '__main__':
    main()

