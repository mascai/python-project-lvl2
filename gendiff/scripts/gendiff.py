import argparse

def main():
    print("Helo world")
    parser = argparse.ArgumentParser()
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.parse_args()


if __name__ == "__main__":
    main()
