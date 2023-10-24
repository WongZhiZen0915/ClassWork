def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    print(arr)
arr = [32,43,65,87,3,1,879,123,45,98,651,381,12,23,94,67,27]
newlist = insertionSort(arr)



def binarys(new):
    import random
    find = False
    n = len(new)
    a = random.randint(0, n-1)
    position = new[a]
    print(position)
    want = int(input("Guess the position of the number(17 position): "))
    while want > n:
        want = int(input("Index out of range:"))
    while not find:
        while want > n:
            want = int(input("Index out of range:"))
        find = False
        if want-1 == a:
            print("You got it!")
            find = True
        elif want-1 < a:
            want = int(input("The number you guess is lower, guess again:"))
        elif want-1 > a:
            want = int(input("The number you guess is too high, guess again: "))

newlist = [1, 3, 12, 23, 27, 32, 43, 45, 65, 67, 87, 94, 98, 123, 381, 651, 879]
binarys(newlist)
