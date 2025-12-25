import sys

def even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    even_odd_checker = EvenOddChecker()
    even_odd_checker.main(sys.argv)