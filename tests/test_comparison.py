import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tictactoe import TicTacToe

def run_comparison():
    game = TicTacToe()
    
    # Test position (X to move on a partially filled board)
    # X | O | X
    #   | O |  
    #   |   |  
    test_board = ['X', 'O', 'X', ' ', 'O', ' ', ' ', ' ', ' ']
    
    print("Evaluating Test Board Position...")
    
    game.nodes_minimax = 0
    score_mm = game.minimax(test_board[:], True)
    
    game.nodes_alphabeta = 0
    print("\n--- Pruning Log ---")
    score_ab = game.alphabeta(test_board[:], True, -1000, 1000, log_pruning=True)
    print("-------------------\n")

    print(f"Plain Minimax Score: {score_mm} | Nodes Expanded: {game.nodes_minimax}")
    print(f"Alpha-Beta Score:    {score_ab} | Nodes Expanded: {game.nodes_alphabeta}")
    
    assert score_mm == score_ab, "Scores do not match!"
    print(f"Verification Successful: Results are identical, but Alpha-Beta reduced search nodes by {((game.nodes_minimax - game.nodes_alphabeta)/game.nodes_minimax)*100:.2f}%")

if __name__ == "__main__":
    run_comparison()
