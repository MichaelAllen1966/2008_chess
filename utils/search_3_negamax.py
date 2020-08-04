import chess
import random

def scoreboard(board, depthleft, evaluate):
    
    """
    
    This method uses a Negated Minimax method. Instead of two subroutines
    for maximising and minimising players, it passes on the negated score due to
    following mathematical relation:

        max(a, b) == -min(-a, -b)

    """
    
    # Note, if it is blacks turn alpha and beta have been reversed.
    
    bestscore = -9999
    
    if depthleft == 0:        
        # Return end leaf
        return (evaluate(board))
    
    # Negated minimax
    for move in board.legal_moves:
        # Get score for each possible move
        board.push(move)   
        # Recurssive depth-first search. This will follow one path down the 
        # search tree until depthleft == 0. The negative reverse white/black
        # each moved
        score = -scoreboard(board, depthleft - 1, evaluate)
        # Restore the previous position.
        board.pop()
        # Record new best score if discovered
        if score > bestscore:
            bestscore = score
    
    # Return best score from the starting position given to alphabeta search
    return bestscore
    

def selectmove(board, depth, evaluate):
    # Return random choice if depth = 0 
    if depth == 0:
        return random.choice(list(board.legal_moves))
    
    bestMove = chess.Move.null()
    bestValue = -99999
    # Iterate through legal moves
    for move in board.legal_moves:
        # Play move
        board.push(move)
        # Get value of move (reduce depth by 1, as 1 move already made)
        # Reverse sign to swap white/black
        boardValue = -scoreboard(board, depth-1, evaluate)
        # Strore move and value if best discovered so far
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        # Restore the previous position
        board.pop()
        
    return bestMove
