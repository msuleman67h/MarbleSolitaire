from typing import Optional


class Peg:
    def __init__(self, peg_num):
        self.parents: list[Optional[Peg]] = [None, None]
        self.children: list[Optional[Peg]] = [None, None]
        self.peg_number: int = peg_num
        self.active: bool = True

    def __hash__(self):
        return hash(f"{self.peg_number}{self.active}{[x for x in self.parents]}{[x for x in self.children]}")

    def set_inactive(self):
        self.active = False
        self.peg_number = -1

    def set_active(self, peg_num):
        self.active = True
        self.peg_number = peg_num

    def get_left_parent(self) -> Optional["Peg"]:
        return self.parents[0]

    def set_left_parent(self, parent: "Peg"):
        self.parents[0] = parent

    def get_right_parent(self) -> Optional["Peg"]:
        return self.parents[1]

    def set_right_parent(self, parent: "Peg"):
        self.parents[1] = parent

    def get_left_child(self) -> Optional["Peg"]:
        return self.children[0]

    def set_left_child(self, peg: "Peg"):
        self.children[0] = peg
        peg.set_right_parent(self)

    def get_right_child(self) -> Optional["Peg"]:
        return self.children[1]

    def set_right_child(self, peg: "Peg"):
        self.children[1] = peg
        peg.set_left_parent(self)

    def can_move_top_left(self) -> bool:
        if self.get_left_parent() is None or self.get_left_parent().get_left_parent() is None:
            return False

        top_left = self.get_left_parent().get_left_parent()
        if self.active and self.get_left_parent().active and not top_left.active:
            return True
        return False

    def move_top_left(self):
        top_left = self.get_left_parent().get_left_parent()
        top_left.set_active(self.peg_number)
        self.get_left_parent().set_inactive()
        self.set_inactive()

    def can_move_top_right(self) -> bool:
        if self.get_right_parent() is None or self.get_right_parent().get_right_parent() is None:
            return False

        top_right = self.get_right_parent().get_right_parent()
        if self.active and self.get_right_parent().active and not top_right.active:
            return True
        return False

    def move_top_right(self):
        top_right = self.get_right_parent().get_right_parent()
        top_right.set_active(self.peg_number)
        self.get_right_parent().set_inactive()
        self.set_inactive()

    def can_move_bottom_left(self) -> bool:
        if self.get_left_child() is None or self.get_left_child().get_left_child() is None:
            return False

        bottom_left = self.get_left_child().get_left_child()
        if self.active and self.get_left_child().active and not bottom_left.active:
            return True
        return False

    def move_bottom_left(self):
        bottom_left = self.get_left_child().get_left_child()
        bottom_left.set_active(self.peg_number)
        self.get_left_child().set_inactive()
        self.set_inactive()

    def can_move_bottom_right(self) -> bool:
        if self.get_right_child() is None or self.get_right_child().get_right_child() is None:
            return False

        bottom_right = self.get_right_child().get_right_child()
        if self.active and self.get_right_child().active and not bottom_right.active:
            return True
        return False

    def move_bottom_right(self):
        bottom_right = self.get_right_child().get_right_child()
        bottom_right.set_active(self.peg_number)
        self.get_right_child().set_inactive()
        self.set_inactive()

    def can_move_left(self) -> bool:
        if self.get_left_parent() is None or self.get_left_parent().get_left_child() is None:
            return False

        adjacent_node = self.get_left_parent().get_left_child()
        if adjacent_node.get_left_parent() is None or adjacent_node.get_left_parent().get_left_child() is None:
            return False

        # If current node is active and the node left to it. But the node left to left node is inactive.
        if self.active and adjacent_node.active and not adjacent_node.get_left_parent().get_left_child().active:
            return True
        return False

    def move_left(self):
        adjacent_node = self.get_left_parent().get_left_child()
        left_node = adjacent_node.get_left_parent().get_left_child()
        left_node.set_active(self.peg_number)
        adjacent_node.set_inactive()
        self.set_inactive()

    def can_move_right(self) -> bool:
        if self.get_right_parent() is None or self.get_right_parent().get_right_child() is None:
            return False

        adjacent_node = self.get_right_parent().get_right_child()
        if adjacent_node.get_right_parent() is None or adjacent_node.get_right_parent().get_right_child() is None:
            return False

        # If current node is active and the node right to it. But the node right to right node is inactive.
        if self.active and adjacent_node.active and not adjacent_node.get_right_parent().get_right_child().active:
            return True
        return False

    def move_right(self):
        adjacent_node = self.get_right_parent().get_right_child()
        right_node = adjacent_node.get_right_parent().get_right_child()
        right_node.set_active(self.peg_number)
        adjacent_node.set_inactive()
        self.set_inactive()

    def __repr__(self) -> str:
        return f"{self.peg_number}: {1 if self.active else 0}"
