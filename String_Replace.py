def split_and_join(line):
    A = line.replace(" ", "-")
    return A
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
