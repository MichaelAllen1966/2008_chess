import chess
import random
from utils.score_basic import evaluate

def scoreboard(board, depthleft, maximising_player):
    
    """
    https://youtu.be/l-hh51ncgDI

    """
    
    if depthleft == 0:        
            # Return end leaf
            
            score = evaluate(board)
            return_score = score if maximising_player else -score
            
            return return_score


    if maximising_player:
        
        max_eval = -999999    

        for move in board.legal_moves:
            # Get score for each possible move
            board.push(move)   
            # Recurssive depth-first search. This will follow one path down the 
            # search tree until depthleft == 0. 
            score = scoreboard(board, depthleft - 1, maximising_player=False )
            # Restore the previous position.
            board.pop()
            # Record new best score if discovered
            if score > max_eval:
                max_eval = score
        
        # Return best score from the starting position given to alphabeta search
        return max_eval
    
    else:
        
        min_eval = 999999
        
        for move in board.legal_moves:
            # Get score for each possible move
            board.push(move)   
            # Recurssive depth-first search. This will follow one path down the 
            # search tree until depthleft == 0. 
            score = scoreboard(board, depthleft - 1, maximising_player=True )
            # Restore the previous position.
            board.pop()
            # Record new best score if discovered
            if score < min_eval:
                min_eval = score
        
        # Return best score from the starting position given to alphabeta search
        return min_eval
        
    

def selectmove(board, depth):
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
        # Returned value is best value for black. More negative better for black
        boardValue = scoreboard(board, depth-1, maximising_player=False)
        # Strore move and value if best discovered so far
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        # Restore the previous position
        board.pop()
        
    return bestMove
