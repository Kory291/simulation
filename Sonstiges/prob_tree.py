from __future__ import annotations

DEFAULT_MAX_DEPTH = 10*100
ball_pool = {
    "green": 3,
    "blue": 2
}

class Tree:

    def __init__(self, pool, depth = DEFAULT_MAX_DEPTH) -> None:
        self.children = []
        self.root = True
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

    # def _get_all_paths(self) -> list[str]:
    #     all_paths = []
    #     for child in self.children:
    #         all_paths.extend(child.get_path(""))
    #     return all_paths

    def _get_all_paths(self) -> list:
        # get the all paths of the tree and return them as a list for further use
        pass

    def get_path(self, path) -> None:
        # Green, Blue, Red, Red
        children_vals = [child.value for child in self.children]
        if path[0] not in children_vals:
            raise ValueError(f"Value {path[0]} not in pool") 
        else:
            for child in self.children:
                if child.value == path[0]:
                    x = child.get_path(path)
                    print("...")

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
        self.root = False
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
    
    # def get_path(self, current_path: str) -> list:
    #     paths = []
    #     val = self.pool.get(self.value, 0) + 1
    #     path = f"{current_path} - {round(self.probability, 7)} -> {self.value}"
    #     if not self.is_last:
    #         for child in self.children:
    #             paths.extend(child.get_path(path))
    #         return paths
    #     if self.is_last:
    #         return [f"{path} = {round(self.global_probability, 7)}"]

    def get_path(self, path) -> list:
        print("..")
        path = []
        if self.current_depth < len(path):
            childs_val = [child.value for child in self.children]
            if path[self.current_depth] not in childs_val:
                raise ValueError(f"{path[self.current_depth]} not in pool")
            for child in self.children:
                if child.value == path[self.current_dapth]:
                    return [self].extend(child.get_path(path))
        return [self]

    def get_parent(self) -> Node:
        pass 


tree = Tree(ball_pool, 3)
tree.get_path(["green", "blue", "green"])
# print(tree.show_all_paths())
