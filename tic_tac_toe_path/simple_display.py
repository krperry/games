game_state = ["X", 1, 2, 3, 4, 5, 6, 7, 8, 9, "X", 0]

print(f" {game_state[1]} | {game_state[2]} | {game_state[3]} ")
print("---|---|---")
print(f" {game_state[4]} | {game_state[5]} | {game_state[6]} ")
print("---|---|---")
print(f" {game_state[7]} | {game_state[8]} | {game_state[9]} ")


game_state[4] = "X"

print(f" {game_state[1]} | {game_state[2]} | {game_state[3]} ")
print("---|---|---")
print(f" {game_state[4]} | {game_state[5]} | {game_state[6]} ")
print("---|---|---")
print(f" {game_state[7]} | {game_state[8]} | {game_state[9]} ")
