import sys

def main(args):
    if len(args) < 2:
        print("Usage: deadlock_detector <input> <output>")
        return
    input = args[0]
    output = args[1]
    with open(input, "r") as f:
        with open(output, "w") as f2:
            for line in f:
                line = line.strip()
                if line.startswith("#") or line.startswith(""): continue
                f2.write(line)
    print("Done")

if __name__ == "__main__":
    main(sys.argv)