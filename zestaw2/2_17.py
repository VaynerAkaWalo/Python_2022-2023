line = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

l = line.split()
print(l)

l.sort(key=str.casefold)
print(l)

l.sort(key=len)
print(l)