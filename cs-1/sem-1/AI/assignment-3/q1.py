# 1. Program to implement Game Playing Algorithms: Minimax and Alpha Beta Pruning.

import math

def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]

    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Two child nodes
            eval = minimax(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Two child nodes
            eval = minimax(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example game tree represented as a leaf node value list
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Depth of the tree
depth = 3  # log2(len(values)) for a complete binary tree
start_node_index = 0

# Minimax without Alpha-Beta Pruning
minimax_result = minimax(depth, start_node_index, True, values, -math.inf, math.inf)

# Alpha-Beta Pruning
alpha_beta_result = minimax(depth, start_node_index, True, values, -math.inf, math.inf)

minimax_result, alpha_beta_result
