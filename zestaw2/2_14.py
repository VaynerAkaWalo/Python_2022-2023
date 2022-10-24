line = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

Max = max(len(word) for word in line.split())
i = (len(word) for word in line.split())

print(list(i).index(Max))
print(Max)
