def hanoi(n, source, destination, auxiliary ):
    if n > 0:
        if n == 1:
            print(source, "->", destination)
            return
        hanoi(n - 1, source, auxiliary, destination)
        print(source, "->", destination)
        hanoi(n - 1, auxiliary, destination, source)

n = 3
print("-----ZADANIE_1-----")
print("-------HANOI-------")
hanoi(n, 'A', 'C', 'B')
