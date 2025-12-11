from day3 import day3

def main():
    with open('test.txt', 'r') as file:
        data = file.read()
    day3(data)
if __name__ == "__main__":
    main()