import heapq
from collections import defaultdict, namedtuple

HuffmanNode = namedtuple('HuffmanNode', ['freq', 'char', 'left', 'right'])

def build_huffman_tree(frequency):
    heap = [HuffmanNode(freq, char, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook=None):
    if codebook is None: codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    frequency = defaultdict(int, {char: data.count(char) for char in set(data)})
    root = build_huffman_tree(frequency)
    huffman_codes = build_codes(root)
    return ''.join(huffman_codes[char] for char in data), huffman_codes

def huffman_decoding(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code, decoded_data = "", []
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""
    return ''.join(decoded_data)

# Get user input
data = input("Enter a string to encode: ")
encoded_data, huffman_codes = huffman_encoding(data)

print("Original Data:", data)
print("Encoded Data:", encoded_data)
print("Huffman Codes:", huffman_codes)
print("Decoded Data:", huffman_decoding(encoded_data, huffman_codes))
