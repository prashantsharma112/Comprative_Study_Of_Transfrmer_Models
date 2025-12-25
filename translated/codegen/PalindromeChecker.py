import sys

def isPalindrome(s):
    if s.isEmpty():
        return True
    if s.charAt(0) == s.charAt(len(s) - 1):
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + input() + " <input>")
        sys.exit(1)

    input = input()
    print("Input: " + input)
    print("Is the input a palindrome? " + isPalindrome(input))