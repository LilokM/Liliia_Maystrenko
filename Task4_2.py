def enough(cap, on, wait):
    # Your code here
    if wait > cap - on:
        return wait - (cap - on)
    else:
        return 0
        print("Can fit all passengers")