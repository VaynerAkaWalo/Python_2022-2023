line = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

first = "".join(x[0] for x in line.split())
last = "".join(x[-1] for x in line.split())

print(first)
print(last)