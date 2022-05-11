# key rotation
key = [
	[1, 0, 1],
	[0, 0, 1],
	[0, 0, 0]
]

print("Rotate 90")
rotated_key = [kr[::-1] for kr in zip(*key)]
for i in rotated_key:
    print(*i, ' ')

print("Rotate 180")
rotated_key = [kr[::-1] for kr in key[::-1]]
for i in rotated_key:
    print(*i, ' ')

print("Rotate -90")
rotated_key = [kr for kr in zip(*key)][::-1]
for i in rotated_key:
    print(*i, ' ')