import sys

ball_pool = {
    "green": 3,
    "blue": 2,
    "red": 5,
    "yellow": 10,
    "orange": 7
}

class Tree:

    def __init__(self, pool, depth) -> None:
        self.children = []
        self.root = None
        self.pool = pool
        self.depth = depth
        for key, val in self.pool.items():
            new_pool = self.pool.copy()
            if val > 1:
                new_pool.update({key: val - 1})
            else:
                new_pool.pop(key)
            self.children.append(
                Node(
                    self,
                    new_pool,
                    val / sum(list(self.pool.values())),
                    key,
                    1,
                    depth
                )
            )

    
    def get_all_paths(self) -> str:
        all_paths = []
        for child in self.children:
            all_paths.extend(child.get_path(""))
        return "\n".join(all_paths)

        

class Node:
    
    def __init__(self, parent, pool, probability, value, current_depth, max_depth) -> None:
        self.parent = parent
        self.children = []
        # self.pool = pool.copy()
        self.pool = pool
        self.is_last = False
        if self.pool == {} or current_depth == max_depth:
            self.is_last = True
        self.probability = probability
        self.value = value
        self.current_depth = current_depth
        self.max_depth = max_depth
        # add children
        if current_depth < max_depth:
            for key, val in self.pool.items():
                new_pool = self.pool.copy()
                if val > 1:
                    new_pool.update({key: val - 1})
                else:
                    new_pool.pop(key)
                self.children.append(
                    Node(
                        self,
                        new_pool,
                        val / sum(list(self.pool.values())),
                        key,
                        current_depth + 1,
                        max_depth
                    )
                )
        
    def is_last(self) -> bool:
        return self.is_last
    
    def get_path(self, current_path: str) -> str:
        paths = []
        path = f"{current_path} {self.value}"
        if not self.is_last:
            for child in self.children:
                paths.extend(child.get_path(path))
            return paths
        if self.is_last:
            return [path]

tree = Tree(ball_pool, 4)
print(tree.get_all_paths())