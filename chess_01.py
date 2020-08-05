import chess
from utils.game_over import is_game_over
from utils.score_1_pieces import evaluate
from utils.search_1_minimax import selectmove


def next_move(board):
    # Get current player
    player = "White" if board.turn else "Black"
    print('Player: ', player)

    # Make black search ahead more
    depth = 1 if board.turn else 2
    
    # Get move
    mov = selectmove(board, depth, evaluate)
    print ('Move: ', mov)
    
    # Make move
    board.push(mov)
    
    # Print board and score
    print ('Score: ', int(evaluate(board)))
    print ()    
    print (board)
    print ()
    
    # Check for end of game
    game_finished, reason = is_game_over(board)    
    if game_finished:
        print ('GAME OVER!!!')
        print (reason)
    
    # Return
    continue_game = not game_finished
    
    return continue_game
    

def play_game():
    """Game loop"""
    CONTINUE = True
    board = chess.Board()
    while CONTINUE:
        CONTINUE = next_move(board)
    
    
# Play game
play_game()
    


