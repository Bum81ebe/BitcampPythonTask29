#greeting #bank #money

def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.strip().lower() == "hello":
        return '0'
    elif greeting.strip().lower() == "h":
        return '20'
    else:
        return '100'


if __name__ == "__main__":
    main()