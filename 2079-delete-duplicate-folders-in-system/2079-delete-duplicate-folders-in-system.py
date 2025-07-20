from collections import defaultdict

class TrieNode:
    def __init__(self, name=""):
        self.name = name
        self.children = dict()
        self.removed = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = TrieNode()

        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode(folder)
                node = node.children[folder]

        subtrees = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            serial = []
            for child in sorted(node.children):
                serial.append(child + "[" + serialize(node.children[child]) + "]")
            subtree_str = ''.join(serial)
            subtrees[subtree_str].append(node)
            return subtree_str

        serialize(root)

        for nodes in subtrees.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.removed = True

        res = []
        def collect(node, path):
            for folder, child in node.children.items():
                if not child.removed:
                    res.append(path + [folder])
                    collect(child, path + [folder])
        collect(root, [])
        return res
