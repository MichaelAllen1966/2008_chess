import chess
import random

# PIECE VALUES

piece_value = {
    'king': 0,
    'pawn': 100,
    'knight': 320,
    'bishop': 330,
    'rook': 500,
    'queen': 900
    }

# PIECE TABLES

pawntable = [
     0,  0,  0,  0,  0,  0,  0,  0,
     5, 10, 10,-20,-20, 10, 10,  5,
     5, -5,-10,  0,  0,-10, -5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
     0,  0,  0,  0,  0,  0,  0,  0
    ]

knightstable = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50
    ]

bishopstable = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -20,-10,-10,-10,-10,-10,-10,-20
    ]

rookstable = [
     0,  0,  0,  5,  5,  0,  0,  0,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
     5, 10, 10, 10, 10, 10, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0
    ]

queenstable = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  5,  5,  5,  5,  5,  0,-10,
      0,  0,  5,  5,  5,  5,  0, -5,
     -5,  0,  5,  5,  5,  5,  0, -5,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
    ]

kingstable = [
     20, 30, 10,  0,  0, 10, 30, 20,
     20, 20,  0,  0,  0,  0, 20, 20,
    -10,-20,-20,-20,-20,-20,-20,-10,
    -20,-30,-30,-40,-40,-30,-30,-20,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30
]


def evaluate(board):
    
    # Check for checkmate
    if board.is_checkmate():
        # Check if it is whites turn
        if board.turn:
            # Black wins
            return -9999
        else:
            # White wins
            return 9999
    
    # Check for stalemate
    if board.is_stalemate():
        return 0
    
    # Check that they are sufficient pieces for one player to win 
    if board.is_insufficient_material():
        return 0
    
    # Get number of each type of piece
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    
    # Score differences in total pieces
    # ---------------------------------
    
    material = (piece_value['pawn'] * (wp-bp) +
                piece_value['knight'] * (wn-bn) +
                piece_value['bishop'] * (wb-bb) +
                piece_value['rook'] * (wr-br) +
                piece_value['queen'] * (wq-bq))
    
    
    # Use piece tables to get adjustments by piece location
    # -----------------------------------------------------
                
    # White pawn adjustment
    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    
    # Subtract black pawn adjustment
    pawnsq += sum([-pawntable[chess.square_mirror(i)] 
                    for i in board.pieces(chess.PAWN, chess.BLACK)])
    
    # White knight adjustment
    knightsq = sum([knightstable[i]
                    for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    
    # Subtract black knigth adjustment
    knightsq += sum([-knightstable[chess.square_mirror(i)] 
                    for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    
    # White bishop adjustment
    bishopsq = sum([bishopstable[i]
                    for i in board.pieces(chess.BISHOP, chess.WHITE)])
    
    # Subtract black bishop adjustment
    bishopsq += sum([-bishopstable[chess.square_mirror(i)] 
                    for i in board.pieces(chess.BISHOP, chess.BLACK)])
    
    # White rook adjustment
    rooksq = sum([rookstable[i]
                    for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    
    # Subtract black rook adjustment
    rooksq += sum([-rookstable[chess.square_mirror(i)] 
                    for i in board.pieces(chess.ROOK, chess.BLACK)])
    
    # White queen adjustment
    queensq = sum([queenstable[i]
                   for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    
    # Subtract black queen adjustment
    queensq += sum([-queenstable[chess.square_mirror(i)] 
                    for i in board.pieces(chess.QUEEN, chess.BLACK)])
    
    # White king adjustment         
    kingsq = sum([kingstable[i]
                  for i in board.pieces(chess.KING, chess.WHITE)]) 
    
    # Subtract black king adjustment
    kingsq += sum([-kingstable[chess.square_mirror(i)] 
                    for i in board.pieces(chess.KING, chess.BLACK)])
                   
    # Add adjustments to score
    score = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    
    # Add random 0-1 to score (to randomize equal scoring moves)
    score += random.random()
    
    # Return score (return -score for black)    
    score_to_return = score if board.turn else -score
    
    return score_to_return

