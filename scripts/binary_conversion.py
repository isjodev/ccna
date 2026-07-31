import sys

binary = (sys.argv[1])

def decimal_conversion(num):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def main():
    print(decimal_conversion(binary))
    exit()

if __name__ == "__main__":
    main()


