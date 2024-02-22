def collatz_sequence(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    print(1)  # Print the final value (1) after the loop

def main():
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input <= 0:
            print("Please enter a positive integer.")
        else:
            collatz_sequence(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
