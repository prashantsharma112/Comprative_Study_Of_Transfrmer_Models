import sys

def main():
    text = sys.stdin.read()
    count = 0
    for char in text:
        if char == '\n':
            count += 1
    print("The character '" + text[0] + "' appears " + count + " times.")

if __name__ == '__main__':
    main()