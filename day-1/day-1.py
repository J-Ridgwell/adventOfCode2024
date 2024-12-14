# read in the file

# Sort columns ascending

# iterate over each pair

# Find difference

# Sum difference


def main():
    """Main function to execute the script logic."""
    print("Hello, World!")

    answer = 0
    list_a = []
    list_b = []

    try:
        with open("/Users/ridgwell1/dev/adventOfCode2024/input.txt", "r") as file:
            for line in file:
                a, b = line.strip().split()
                list_a.append(int(a))
                list_b.append(int(b))
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("An error occurred while reading the file.")
    except ValueError:
        print("list contains not a number")

    list_a.sort()
    list_b.sort()

    for a, b in zip(list_a, list_b):
        answer += abs(a - b)

    print(answer)


# Entry point
if __name__ == "__main__":
    main()
