enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"Number of enemies : {enemies}")

increase_enemies()
print(f"Number of Enemies Now : {enemies}")