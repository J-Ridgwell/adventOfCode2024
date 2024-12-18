import re


def main():
    """Main function to execute the script logic."""

    regex = "mul\\((\\d*),(\\d*)\\)"

    with open("day-3/input.txt", "r") as f:
        content = f.read()

    matches = re.findall(re.compile(regex), content)

    if matches == None:
        print("No matches found")
        return

    sum1 = 0
    for x, y in matches:
        sum1 += int(x) * int(y)

    print(sum1)
    print(sum(int(x) * int(y) for x, y in matches))


# Entry point
if __name__ == "__main__":
    main()
