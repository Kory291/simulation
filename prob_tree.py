import sys


DEFAULT_MAX_DEPTH = 10*100
ball_pool = {
    "green": 3,
    "blue": 2
}

class Tree:

    def __init__(self, pool, depth = DEFAULT_MAX_DEPTH) -> None:
        self.children = []
        self.root = None
        self.pool = pool
        self.depth = depth
        self.global_probability = 1
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

    
    def show_all_paths(self) -> str:
        return "\n".join(self._get_all_paths())

    def _get_all_paths(self) -> list[str]:
        all_paths = []
        for child in self.children:
            all_paths.extend(child.get_path(""))
        return all_paths

    def get_path(self, path):
        pass

    def get_probability_of_path(self, path):
        pass

    def test_probabilities(self):
        # Ensure the sum of all global probabilities is equal to 1
        pass
        

class Node:
    
    def __init__(self, parent, pool, probability, value, current_depth, max_depth) -> None:
        self.parent = parent
        self.children = []
        self.pool = pool
        self.is_last = False
        if self.pool == {} or current_depth == max_depth:
            self.is_last = True
        self.probability = probability
        self.global_probability = self.probability * self.parent.global_probability
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
        val = self.pool.get(self.value, 0) + 1
        path = f"{current_path} - {round(self.probability, 7)} -> {self.value}"
        if not self.is_last:
            for child in self.children:
                paths.extend(child.get_path(path))
            return paths
        if self.is_last:
            return [f"{path} = {round(self.global_probability, 7)}"]

tree = Tree(ball_pool)
print(tree.show_all_paths())