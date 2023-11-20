import fib

def main():
    print(f"Hello! The first ten fibonacci numbers are the following:")

    for i in range(10):
        print(f"fib({i}) = {fib.fib(i)}")


if __name__ == "__main__":
    main()
