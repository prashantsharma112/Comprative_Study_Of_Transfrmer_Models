import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python max_of_three.py first_number second_number third_number")
        sys.exit(1)

    first = int(input())
    second = int(input())
    third = int(input())

    if first > second or second > third:
        print("The largest number is: " + first)
        print("The smallest number is: " + second)
        print("The largest number is: " + third)
        sys.exit(1)

    print("The largest number is: " + first)
    print("The smallest number is: " + second)
    print("The largest number is: " + third)

if __name__ == "__main__":
    main()