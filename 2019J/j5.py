# Rule of Three
# Read in the input
t1, d1 = input().split()
t2, d2 = input().split()
t3, d3 = input().split()
MOVES = [(t1, d1), (t2, d2), (t3, d3)] 
steps, src, target = input().split()
steps = int(steps)

# Main dfs/recursion
visited = set()
moves = []

def dfs(steps_left, state):
    # No more moves left (BASE CASE 1)
    if steps_left == 0:
        return state == target

    # Already visited? (BASE CASE 2)
    node = (steps_left, state)
    if node in visited:
        return False
    visited.add(node) # Add to already explored

    # Go through each rule (find the "neighbors")
    for rule_id, (A, B) in enumerate(MOVES, 1):
        # Find all potential positions to apply the rule
        pos = -1
        while True:
            # Find next occurrence of pattern A
            pos = state.find(A, pos + 1)
            if pos == -1: # If it doesn't find anything
                break
            # Create the new replaced sequence
            new_state = state[:pos] + B + state[pos + len(A):]
            # Add to set of moves used
            moves.append((rule_id, pos, new_state))
            # Does this lead us to the target string?
            if dfs(steps_left - 1, new_state):
                return True
            # This move is bad, remove it
            moves.pop()
    # Current node (# of steps used, current pattern) does not work
    return False

dfs(steps, src)

# Print out the required moves
for i, j, k in moves:
    print(i, j + 1, k)
