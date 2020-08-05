import chess
import random

def scoreboard(board, depthleft, evaluate, maximising_player):
    
    """
    Minimax tree search.
    
    If the search starts from the perspective of the maximising player, the 
    maximum score will be returned.
    
    If the search starts from the perspective of the minimising player, the 
    miniumum score will be returned.
    
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
            score = scoreboard(
                board, depthleft - 1, evaluate, maximising_player=False )
            # Restore the previous position.
            board.pop()
            # Record new best score if discovered
            if score > max_eval:
                max_eval = score
        
        # Return best score 
        return max_eval
    
    else:
        
        min_eval = 999999
        
        for move in board.legal_moves:
            # Get score for each possible move
            board.push(move)   
            # Recurssive depth-first search. This will follow one path down the 
            # search tree until depthleft == 0. 
            score = scoreboard(
                board, depthleft - 1, evaluate, maximising_player=True )
            # Restore the previous position.
            board.pop()
            # Record new best score if discovered
            if score < min_eval:
                min_eval = score
        
        # Return best score from the starting position given to alphabeta search
        return min_eval
        
    

def selectmove(board, depth, evaluate):
    """
    This algorithm loops through all legal moves. From ecah of these starting
    positions the board is evaluated by minimax tree search from the perspective
    of the opposing player. The opposing player is looking to minimise the board
    score (maximise negative score), so the maximum value found in the tree
    serach will be the worst posiiton for the opposing player.
    """
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
        # Returned value is best value for opposing player where higher value
        # (less negative) is worse for opposing player. 
        boardValue = scoreboard(
            board, depth-1, evaluate, maximising_player=False)
        # Strore move and value if best discovered so far
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        # Restore the previous position
        board.pop()
        
    return bestMove
