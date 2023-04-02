# \t为制表符，可以使文本对齐
i = 0
j = 1
while i <= 9:
    while j <= i:
        print(f"\t{j}x{i}={j * i}", end=" ")
        j += 1
    print()
    j = 1
    i += 1