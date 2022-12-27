def infiniteRecursion(num):
    # Base Case
    if (num == 12):
        print("num: ", num)
        return
    # Recursion
    print("num: ", num)
    num += 1
    infiniteRecursion(num)

if __name__ == "__main__":
    infiniteRecursion(15)