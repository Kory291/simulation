pool = {
    "green": 3,
    "blue": 2,
    "red": 5
}

class Node:
    
    _pool: dict
    _children: list
    _probability: float
    _value: str

    def __init__(self, value: str, pool: dict):
        self._pool = pool.copy()
        print(id(pool), id(self._pool))
        self._value = value
        all_elements = sum(list(self._pool.values()))
        self._probability = self._pool.get(self._value) / all_elements
        if self._pool.get(self._value) > 1:
            self._pool.update({self._value: self._pool.get(self._value) - 1})
        else:
            self._pool.pop(self._value)
        self._children = []
        for key, val in self._pool.items():
            self._children.append(Node(key, self._pool))
            
    def _isLast(self):
        return len(list(self._pool.items())) == 0

Node("green", pool)