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


def evaluate(board):

    """
    The function returns the score from the perdsepctive of the maximising
    player.
    """
    
    # Create dictionary of value of pieces
    piece_value = {
    'king': 0,
    'pawn': 100,
    'knight': 320,
    'bishop': 330,
    'rook': 500,
    'queen': 900}
    
    # Check for checkmate
    if board.is_checkmate():
        # Check if it is whites turn
        if board.turn:
            score = -9999
        else:
            score = 9999
    
    # Check for stalemate
    elif board.is_stalemate():
        score = 0
    
    # Check that they are sufficient pieces for one player to win 
    elif board.is_insufficient_material():
        return 0
    
    else:
        # Score py pieces
    
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
        score = (piece_value['pawn'] * (wp-bp) +
                 piece_value['knight'] * (wn-bn) +
                 piece_value['bishop'] * (wb-bb) +
                 piece_value['rook'] * (wr-br) +
                 piece_value['queen'] * (wq-bq))
         
    # Add random 0-1 to score (to randomize equal scoring moves)
    score += random.random()
    
    # Return score (return -score for black)
    
    score_to_return = score if board.turn else -score
    
    return score_to_return

