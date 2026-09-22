def encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    grid = [[""] * cols for _ in range(rows)]

    index = 0

    for row in range(rows):
        for col in range(cols):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    order = sorted(range(cols), key=lambda x: int(key[x]))

    encrypted = ""

    for col in order:
        for row in range(rows):
            if grid[row][col] != "":
                encrypted += grid[row][col]

    return encrypted


def decrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    order = sorted(range(cols), key=lambda x: int(key[x]))

    grid = [[""] * cols for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    decrypted = ""

    for row in range(rows):
        for col in range(cols):
            decrypted += grid[row][col]

    return decrypted


text = "COMPUTER"
key = "3142"

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)