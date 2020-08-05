def is_game_over(board):
    """Check whether game is over"""
    
    reason = ''
    game_over = board.is_game_over()
    
    
    if game_over:
        if board.is_checkmate():
            reason  = 'Checkmate'
        elif board.is_stalemate():
            reason = 'Stalemate'
        elif board.is_insufficient_material:
            reason = 'Insufficient material'
        elif board.is_fivefold_repetition():
            reason = 'Five fold repitition'
        else:
            reason = 'Other'
            
    return game_over, reason
