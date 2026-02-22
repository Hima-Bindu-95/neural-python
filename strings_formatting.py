def print_formatted(number):
    # your code goes here
    n=(len(bin(number)[2:]))
    for i in range(number):
     print(f"{i+1:{n}d} {oct(i+1)[2:]:>{n}} {hex(i+1)[2:].upper():>{n}} {bin(i+1)[2:]:>{n}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
