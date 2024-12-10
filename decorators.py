from functools import wraps

def game_over_check(battle_func):
    """
    Decorator to check if the player died in battle and end the game if they did.
    """
    @wraps(battle_func)
    def wrapper(player, *args, **kwargs):
        battle_func(player, *args, **kwargs)  # Call the battle function
        if player.hp <= 0:
            print("Game Over.")
            exit()  # Terminate the game
    return wrapper