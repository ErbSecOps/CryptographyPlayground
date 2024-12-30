import string

ENGLISH_CHAR_FREQUENCIES = {
    'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270,
    'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015,
    'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751,
    'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
    'u': 0.0276, 'v': 0.0098, 'w': 0.0237, 'x': 0.0015, 'y': 0.0197,
    'z': 0.0007
}

def shift_char(char, key):
    if char.isalpha():
        alpha_start = ord('a')
        alpha_size = 26
        shifted = (ord(char.lower()) - alpha_start + key) % alpha_size + alpha_start
        return chr(shifted).upper() if char.isupper() else chr(shifted)
    else:
        return char

def caesar_shift(text, key):
    return ''.join(shift_char(ch, key) for ch in text)

def compute_frequency_distribution(text):
    text_lower = text.lower()
    counts = dict.fromkeys(string.ascii_lowercase, 0)
    total_letters = 0
    for ch in text_lower:
        if ch in counts:
            counts[ch] += 1
            total_letters += 1
    if total_letters == 0:
        return {letter: 0.0 for letter in string.ascii_lowercase}
    return {letter: counts[letter] / total_letters for letter in string.ascii_lowercase}

def frequency_least_squares_score(observed_freq, expected_freq):
    score = 0.0
    for letter in string.ascii_lowercase:
        diff = observed_freq.get(letter, 0.0) - expected_freq.get(letter, 0.0)
        score += diff**2
    return score

def crack_caesar_cipher(ciphertext):
    best_shift = 0
    min_score = float('inf')
    for key in range(26):
        shifted_text = caesar_shift(ciphertext, -key)
        observed_freq = compute_frequency_distribution(shifted_text)
        score = frequency_least_squares_score(observed_freq, ENGLISH_CHAR_FREQUENCIES)
        if score < min_score:
            min_score = score
            best_shift = -key
    decrypted_text = caesar_shift(ciphertext, best_shift)
    return best_shift, decrypted_text

if __name__ == "__main__":
    encrypted = "Q Squiqh iqbqt yi q whuud iqbqt ev hecqydu bujjksu qdt shekjedi thuiiut myjx buced zkysu."
    shift_found, plaintext = crack_caesar_cipher(encrypted)
    print(f"Best Shift: {shift_found}")
    print(f"Plaintext: {plaintext}")
