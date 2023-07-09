class ClassNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

class ClassHierarchy:
    def __init__(self):
        self.classes = {}

    def add_class(self, name, parent_name=None):
        node =  self.classes.get(name)
        if not node:
            node = ClassNode(name)
            self.classes[name] = node

        if parent_name is not None:
            parent_node = self.classes.get(parent_name)
            if not parent_node:
                parent_node = ClassNode(parent_name)
            
            node.parent = parent_node
            parent_node.children.append(node)

    def find_sibling_classes(self, class_name):
        parent_node = self.classes[class_name].parent
        if parent_node is None:
            return []

        siblings = []
        for child_node in parent_node.children:
            if child_node.name != class_name:
                siblings.append(child_node.name)
        return siblings

    def find_parent_class(self, class_name):
        parent_node = self.classes[class_name].parent
        if parent_node is None:
            return None
        return parent_node.name

    def find_ancestor_classes(self, class_name):
        node = self.classes[class_name]
        ancestors = []

        while node.parent is not None:
            node = node.parent
            ancestors.append(node.name)

        return ancestors

    def check_common_ancestors(self, class_name1, class_name2):
        ancestors1 = set(self.find_ancestor_classes(class_name1))
        ancestors2 = set(self.find_ancestor_classes(class_name2))

        common_ancestors = ancestors1.intersection(ancestors2)
        return len(common_ancestors) > 0