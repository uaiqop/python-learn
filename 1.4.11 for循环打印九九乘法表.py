for y in range(1, 10):
    for x in range(1, y + 1):
        print(f"\t{x}x{y}={x * y}", end=" ")
    print()