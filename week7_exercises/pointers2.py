scores = [85, 92, 78, 95, 60]
offset = 0

print("--- 2. Forward Traversal ---")
while offset < len(scores):
    print(scores[offset])
    offset += 1

print("\n--- 3. Find Maximum Value ---")
max_val = scores[0]
offset = 1

while offset < len(scores):
    if scores[offset] > max_val:
        max_val = scores[offset]
    offset += 1

print(f"Maximum value: {max_val}")

print("\n--- 4. Reverse Traversal ---")
offset = len(scores) - 1

while offset >= 0:
    print(scores[offset])
    offset -= 1


print("\n--- 5. Bonus: Pointer/Reference Behavior ---")

ptr = scores 

print(f"Original scores[2]: {scores[2]}")

ptr[2] = 100

print(f"Modified ptr[2]: {ptr[2]}")
print(f"Does scores[2] change? {scores[2]}")  
print(f"id(ptr) == id(scores): {id(ptr) == id(scores)}") 
