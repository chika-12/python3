#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of arguments of a list"""
    import args

    count = len(args.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, args.argv[i + 1]))
