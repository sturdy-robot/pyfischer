from .pieces import Pieces


class Board:
    def __init__(self):
        self.board = [
            [i + 8 * j for i in range(8)]
            for j in range(8)
        ]
        self.square_files = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H'
        ]
        self.squares = [
            [sq + str(i+1) for sq in self.square_files]
            for i in range(8)
        ]
        self.sq_to_board = self.square_to_board()
        self.playboard = []

    def setup_board(self):
        for rank, square in enumerate(self.board):
            if rank == 0:
                self.playboard.append([
                    Pieces.WROOK,
                    Pieces.WKNIGHT,
                    Pieces.WBISHOP,
                    Pieces.WQUEEN,
                    Pieces.WKING,
                    Pieces.WBISHOP,
                    Pieces.WKNIGHT,
                    Pieces.WROOK
                ])
            elif rank == 1:
                self.playboard.append(
                    [Pieces.WPAWN for _ in range(8)]
                )
            elif rank == 6:
                self.playboard.append(
                    [Pieces.BPAWN for _ in range(8)]
                )
            elif rank == 7:
                self.playboard.append([
                    Pieces.BROOK,
                    Pieces.BKNIGHT,
                    Pieces.BBISHOP,
                    Pieces.BQUEEN,
                    Pieces.BKING,
                    Pieces.BBISHOP,
                    Pieces.BKNIGHT,
                    Pieces.BROOK
                ])

    def square_to_board(self):
        sq_to_board = {}
        for row_sq, row_ind in zip(self.squares, self.board):
            for index_sq, index_num in zip(row_sq, row_ind):
                sq_to_board[index_sq] = row_ind[index_num]

        return sq_to_board


class BitBoard:
    def __init__(self):
        pass
