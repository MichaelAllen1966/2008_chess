import chess
import random

def scoreboard(board, depthleft, alpha, beta, evaluate, maximising_player):
    
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
            score = scoreboard(board, depthleft-1, alpha, beta, evaluate, 
                               maximising_player=False )
            # Restore the previous position.
            board.pop()
            # Record new best score if discovered
            if score > max_eval:
                max_eval = score
            # Update alpha:
            if score > alpha:
                alpha = score
            # Break loop if beta lower than alpha
            if beta <= alpha:
                break
        
        # Return best score from the starting position given to alphabeta search
        return max_eval
    
    else:
        
        min_eval = 999999
        
        for move in board.legal_moves:
            # Get score for each possible move
            board.push(move)   
            # Recurssive depth-first search. This will follow one path down the 
            # search tree until depthleft == 0. 
            score = scoreboard(board, depthleft-1, alpha, beta, evaluate, 
                               maximising_player=True )
            # Restore the previous position.
            board.pop()
            # Record new best score if discovered
            if score < min_eval:
                min_eval = score
            # Update beta:
            if score < beta:
                beta = score
            # Break loop if beta lower than alpha
            if beta <= alpha:
                break
        
        # Return best score from the starting position given to alphabeta search
        return min_eval
        
    

def selectmove(board, depth, evaluate):
    # Return random choice if depth = 0 
    if depth == 0:
        return random.choice(list(board.legal_moves))
    
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    # Iterate through legal moves
    for move in board.legal_moves:
        # Play move
        board.push(move)
        boardValue = scoreboard(
            board, depth-1, alpha, beta, evaluate, maximising_player=False)
        # Strore move and value if best discovered so far
        # Returned value is best value for black. More negative better for black
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        # Update alpha (pruning value) if new score is better than current
        if boardValue > alpha:
            alpha = boardValue
        # Restore the previous position
        board.pop()
        
    return bestMove
