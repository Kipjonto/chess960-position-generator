from random import randint

def generate_position():
    position = ['♖', '♔', '♖']
    unplaced_pieces = ['♗', '♘', '♘', '♕']
    for i in range(4):
        piece = unplaced_pieces.pop()
        index = randint(0, len(position)-1)
        position.insert(index, piece)
    # Bishops must be on even and odd indexes
    bishopIndex = position.index('♗')
    secondBishopIndex = randint(bishopIndex + 1, len(position))
    if (bishopIndex % 2 == secondBishopIndex % 2):
        secondBishopIndex -= 1
    position.insert(secondBishopIndex, '♗')
    return position

print(generate_position())
