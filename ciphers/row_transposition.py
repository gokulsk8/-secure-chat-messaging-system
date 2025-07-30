def encrypt(text, key):
    key = [int(k) for k in key]
    col_count = len(key)
    
    # Remove spaces and convert to uppercase (optional but recommended)
    text = text.replace(" ", "").upper()
    
    # Pad text with 'X' to fit the matrix
    while len(text) % col_count != 0:
        text += 'X'
    
    # Break into rows
    rows = [text[i:i + col_count] for i in range(0, len(text), col_count)]
    
    # Determine order of columns based on key
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    
    # Read columns in the key order
    encrypted = ''
    for i in key_order:
        for row in rows:
            encrypted += row[i]
    
    return encrypted


def decrypt(cipher, key):
    key = [int(k) for k in key]
    col_count = len(key)
    row_count = len(cipher) // col_count

    # Determine key order
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    
    # Prepare empty columns list
    cols = [''] * col_count
    k = 0

    # Fill columns in the correct order
    for i in key_order:
        cols[i] = cipher[k:k + row_count]
        k += row_count

    # Reconstruct plaintext row by row
    decrypted = ''
    for r in range(row_count):
        for c in range(col_count):
            decrypted += cols[c][r]
    
    return decrypted.rstrip('X')  # Remove padding
