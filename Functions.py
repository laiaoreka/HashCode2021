def recursive(number):
    number -= 1
    if number > 0:
        print(number)
        recursive(number)
    else:
        print("stop")
        breakpoint()

    return number