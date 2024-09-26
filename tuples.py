if __name__ == '__main__':
    n = int(input())  # Read the integer n
    integer_list = map(int, input().split())  # Read the space-separated integers
    t = tuple(integer_list)  # Create a tuple
    print(hash(t))  # Print the hash of the tuple
