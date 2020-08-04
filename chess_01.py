import chess
from utils.score_1_pieces import evaluate
from utils.search_1_minimax import selectmove


def next_move(board):
    # Get current player
    player = "White" if board.turn else "Black"
    print('Player: ', player)
    
    # Set default value for game finished
    game_finished = False
    
    #make black search ahead more
    depth = 0 if board.turn else 2
    
    # Get move
    mov = selectmove(board, depth, evaluate)
    print ('Move: ', mov)
    
    # Make move
    board.push(mov)
    print ('Score: ', int(evaluate(board)))
    print ()
    
    # Check for checkmate ands stalemate
    if board.is_checkmate():
        print('Checkmate!!')
        game_finished = True
    if board.is_stalemate():
        print('Stalemate')
        game_finished = True
        
    # Print board
    print (board)
    print ()
    
    # Return
    continue_game = not game_finished
    
    return continue_game
    


CONTINUE = True
board = chess.Board()
while CONTINUE:
    CONTINUE = next_move(board)
    
    


