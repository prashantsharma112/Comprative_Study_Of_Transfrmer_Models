import sys

def main(args):
    if len(args) < 2:
        print("Usage: python <command> <input>")
        return
    cmd = args[1]
    input = args[2]
    if cmd == "input":
        print(input)
    elif cmd == "print":
        print(input)
    else:
        print("Unknown command: " + cmd)

if __name__ == "__main__":
    main(sys.argv)