from copy import deepcopy
from dataclasses import dataclass
from pprint import pprint
from queue import Queue

from board import Board


@dataclass
class Game:
    board: Board
    moves: list

    def __hash__(self):
        return hash(self.board)


def main():
    total_num_pegs = 15
    board = Board(number_of_pegs=total_num_pegs, starting_point=0)
    initial_game = Game(board=board, moves=[])

    bfs_queue = Queue()
    visited_games = {}

    # Adding the first game
    bfs_queue.put(initial_game)
    visited_games[initial_game] = initial_game.moves

    sol_found = False

    while not bfs_queue.empty():
        game_instance: Game = bfs_queue.get()

        if game_instance.board.active_pegs == 1:
            print("Won the game")
            print(game_instance.board)
            pprint(game_instance.moves)
            sol_found = True
            break

        for i in range(total_num_pegs):
            # Empty spots cannot jump so no point checking them
            if not game_instance.board.peg_list[i].active:
                continue

            if game_instance.board.peg_list[i].can_move_top_left():
                next_game_state = deepcopy(game_instance)
                next_game_state.board.peg_list[i].move_top_left()
                next_game_state.moves.append(f"{i} to top left diagonally")

                if next_game_state not in visited_games:
                    next_game_state.board.active_pegs -= 1
                    visited_games[next_game_state] = next_game_state.moves
                    bfs_queue.put(next_game_state)

            if game_instance.board.peg_list[i].can_move_top_right():
                next_game_state = deepcopy(game_instance)
                next_game_state.board.peg_list[i].move_top_right()
                next_game_state.moves.append(f"{i} to top right diagonally")

                if next_game_state not in visited_games:
                    next_game_state.board.active_pegs -= 1
                    visited_games[next_game_state] = next_game_state.moves
                    bfs_queue.put(next_game_state)

            if game_instance.board.peg_list[i].can_move_bottom_left():
                next_game_state = deepcopy(game_instance)
                next_game_state.board.peg_list[i].move_bottom_left()
                next_game_state.moves.append(f"{i} to bottom left diagonally")

                if next_game_state not in visited_games:
                    next_game_state.board.active_pegs -= 1
                    visited_games[next_game_state] = next_game_state.moves
                    bfs_queue.put(next_game_state)

            if game_instance.board.peg_list[i].can_move_bottom_right():
                next_game_state = deepcopy(game_instance)
                next_game_state.board.peg_list[i].move_bottom_right()
                next_game_state.moves.append(f"{i} to bottom right diagonally")

                if next_game_state not in visited_games:
                    next_game_state.board.active_pegs -= 1
                    visited_games[next_game_state] = next_game_state.moves
                    bfs_queue.put(next_game_state)

            if game_instance.board.peg_list[i].can_move_left():
                next_game_state = deepcopy(game_instance)
                next_game_state.board.peg_list[i].move_left()
                next_game_state.moves.append(f"{i} to left horizontally")

                if next_game_state not in visited_games:
                    next_game_state.board.active_pegs -= 1
                    visited_games[next_game_state] = next_game_state.moves
                    bfs_queue.put(next_game_state)

            if game_instance.board.peg_list[i].can_move_right():
                next_game_state = deepcopy(game_instance)
                next_game_state.board.peg_list[i].move_right()
                next_game_state.moves.append(f"{i} to right horizontally")

                if next_game_state not in visited_games:
                    next_game_state.board.active_pegs -= 1
                    visited_games[next_game_state] = next_game_state.moves
                    bfs_queue.put(next_game_state)

    if not sol_found:
        print("No solutions were found :(")


if __name__ == '__main__':
    main()
