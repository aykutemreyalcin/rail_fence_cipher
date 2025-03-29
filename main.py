def encode_rail_fence_cipher(string, n):
    rail_array = [i for i in range(1,n+1)]
    rail_array.extend([i for i in range(n-1,0,-1)])
    obj = {}
    for i in range(1,n+1):
        obj["l"+str(i)] = []
    while len(string) > len(rail_array):
        rail_array.extend(rail_array[1::])
    for i in range(1,len(string)+1):
        obj["l"+str(rail_array[i-1])].extend(string[i-1])
    final_list = []
    for i in obj.values():
        final_list.extend(i)
    return "".join(final_list)

def decode_rail_fence_cipher(cipher_text, n):
    if n == 1:
        return cipher_text

    rail_pattern = list(range(n)) + list(range(n - 2, 0, -1))

    rail_lengths = [0] * n
    for i in range(len(cipher_text)):
        rail_lengths[rail_pattern[i % len(rail_pattern)]] += 1

    rails = []
    index = 0
    for length in rail_lengths:
        rails.append(list(cipher_text[index:index + length]))
        index += length

    result = []
    rail_positions = [0] * n
    for i in range(len(cipher_text)):
        rail_index = rail_pattern[i % len(rail_pattern)]
        result.append(rails[rail_index][rail_positions[rail_index]])
        rail_positions[rail_index] += 1

    return "".join(result)