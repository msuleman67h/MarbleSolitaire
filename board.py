from peg import Peg


class Board:
    def __init__(self, number_of_pegs, starting_point):
        self.peg_list = [Peg(i) for i in range(number_of_pegs)]
        self.offset_indices = [0]
        index = 0
        shift = 2
        while index < number_of_pegs - 1:
            index += shift
            self.offset_indices.append(index)
            shift += 1

        # Manually Setting the children of first node
        self.board = self.peg_list[0]
        self.board.set_left_child(self.peg_list[1])
        self.board.set_right_child(self.peg_list[2])

        # Inserting the remaining pegs
        offset = 0
        for index, peg in enumerate(self.peg_list[1:]):
            try:
                peg.set_left_child(self.peg_list[1:][index + 2 + offset])
                peg.set_right_child(self.peg_list[1:][index + 3 + offset])
                if index + 1 in self.offset_indices:
                    offset += 1
            except IndexError:
                continue

        self.active_pegs: int = number_of_pegs - 1
        # The top most peg will be our starting position
        self.peg_list[starting_point].set_inactive()

    def __hash__(self):
        return hash(tuple(hash(x) for x in self.peg_list))

    def __str__(self):
        temp = ""
        for index, peg in enumerate(self.peg_list):
            temp = f"{temp} {peg}"

            if index in self.offset_indices:
                temp = f"{temp}\n"
        return temp
