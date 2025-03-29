### README.md

```markdown
# Rail Fence Cipher Encoder/Decoder

This project contains two functions: `encode_rail_fence_cipher` and `decode_rail_fence_cipher`, which implement the Rail Fence Cipher encoding and decoding logic respectively.

## What is the Rail Fence Cipher?

The **Rail Fence Cipher** is a form of transposition cipher. It writes the message in a zigzag pattern (like a rail fence), and then reads off each rail row-wise to form the encoded message. Decoding reverses this process.

---

## Functions

### `encode_rail_fence_cipher(string, n)`

Encodes a given string using the Rail Fence Cipher with `n` rails.

#### Parameters:
- `string`: The plain text to be encoded.
- `n`: Number of rails.

#### Returns:
- Encoded string (cipher text).

---

### `decode_rail_fence_cipher(cipher_text, n)`

Decodes a given Rail Fence Cipher text back to the original plain text.

#### Parameters:
- `cipher_text`: The encoded text.
- `n`: Number of rails.

#### Returns:
- Decoded string (original message).

---

## Example

```python
encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)
# Output: "WECRLTEERDSOEEFEAOCAIVDEN"

decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3)
# Output: "WEAREDISCOVEREDFLEEATONCE"
```

---

## Codewars Kata

This implementation is a solution to a **Codewars Kata** challenge.

- Kata Link: [Rail Fence Cipher: Encoding and Decoding (Codewars)](https://www.codewars.com/kata/58c5577d61aefcf3ff000081)
- Level: 3 kyu
- This code was adapted or used for solving the kata as part of practicing algorithmic thinking and Python coding.

---

## Requirements

- Python 3.x

---

## File Structure

```
rail_fence_cipher/
├── rail_fence.py     # Python code with encode/decode functions
└── README.md         # This file
```
