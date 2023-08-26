from random import randint

def generate_position():
    position = ['♖', '♔', '♖']
    non_placed_pieces = ['♗', '♘', '♘', '♕']

    for i in range(4):
        piece = non_placed_pieces.pop()
        index = randint(0, len(position)-1)
        position.insert(index, piece)

    bishopIndex = position.index('♗')
    secondBishopIndex = randint(bishopIndex + 1, len(position))

    if (bishopIndex % 2 == secondBishopIndex % 2):
        secondBishopIndex -= 1

    position.insert(secondBishopIndex, '♗')

    return position

print(generate_position())
