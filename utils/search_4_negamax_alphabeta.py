import chess
import random

def alphabeta(board, alpha, beta, depthleft, evaluate):
    
    """
    The algorithm maintains two values, alpha and beta, which represent the 
    minimum score that the maximizing player is assured of and the maximum 
    score that the minimizing player is assured of respectively. Initially, 
    alpha is negative infinity and beta is positive infinity, i.e. both 
    players start with their worst possible score. Whenever the maximum score
    that the minimizing player (i.e. the "beta" player) is assured of becomes
    less than the minimum score that the maximizing player (i.e., the "alpha" 
    player) is assured of (i.e. beta < alpha), the maximizing player need not
    consider further descendants of this node, as they will never be reached in
    the actual play (if best moves are followed).
    
    In summary:
    Alpha = best explored option along the path to the root for the maximizer
    Beta = best already explored option along path to the root for the minimizer
    
    Worked detailed example of alpha beta pruning.
    https://youtu.be/xBXHtz4Gbdo
    
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
        # search tree until depthleft == 0. The negatives and reversal of 
        # alpha/beta order alternate views of white + black players
        score = -alphabeta(board, -beta, -alpha, depthleft-1, evaluate )
        # Restore the previous position.
        board.pop()
        # Score is better than beta so other player would not follow this route
        if score >= beta:
            return score
        # Record new best score if discovered
        if score > bestscore:
            bestscore = score
        # Update alpha if score is best explored option on this path
        if score > alpha:
            alpha = score   
    
    # Return best score from the starting position given to alphabeta search
    return bestscore
    

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
        # Get value of move (reduce depth by 1, as 1 move already made)
        # Exchange, and reverse sign for, alpha and beta in call
        boardValue = -alphabeta(board, -beta, -alpha, depth-1, evaluate)
        # Strore move and value if best discovered so far
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        # Update alpha (pruning value) if new score is better than current
        if boardValue > alpha:
            alpha = boardValue
        # Restore the previous position
        board.pop()
        
    return bestMove
