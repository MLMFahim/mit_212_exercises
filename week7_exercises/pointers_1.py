scores = [85, 92, 78, 95, 60]
offset = 0

# Traverse (simulate *(ptr+i))
while offset < len(scores):
    print(scores[offset])
    offset += 1

# Find max using offset
max_val = scores[0]
offset = 1
while offset < len(scores):
    if scores[offset] > max_val:
        max_val = scores[offset]
    offset += 1
