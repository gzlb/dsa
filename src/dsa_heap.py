class Heap:
    def __init__(self):
        self.items = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2

    def swap(self, i, j) -> None:
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def heapify_up(self, index) -> None:
        parent_idx = self.parent(index)
        if index > 0 and self.items[index] < self.items[parent_idx]:
            self.swap(index, parent_idx)
            self.heapify_up(parent_idx)

    def heapify_down(self, index) -> None:
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        if left < len(self.items) and self.items[left] < self.items[smallest]:
            smallest = left
        if right < len(self.items) and self.items[right] < self.items[smallest]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def insert(self, data) -> None:
        self.items.append(data)
        self.heapify_up(len(self.items) - 1)

    def extract_root(self):
        if not self.is_empty():
            root = self.items[0]
            last_element = self.items.pop()
            if not self.is_empty():
                self.items[0] = last_element
                self.heapify_down(0)
            return root
        else:
            raise IndexError("Heap is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
