from adventOfCode.unmarshaller import unmarshal


def main():
    """Main function to execute the script logic."""
    input = unmarshal("day-2/input.txt")
    count = 0
    for line in input:
        count += isSafeImproved(line)

    print(f"Number of safe reports: {count}")


def isSafe(line):
    for i in range(1, len(line) - 1):
        currStep = line[i + 1] - line[i]
        prevStep = line[i] - line[i - 1]

        if (
            abs(prevStep) < 1
            or abs(prevStep) > 3
            or abs(currStep) < 1
            or abs(currStep) > 3
        ):
            return 0

        if currStep > 0 and prevStep < 0 or currStep < 0 and prevStep > 0:
            return 0

    return 1


def isSafeImproved(line):
    def is_valid_step_size(step):
        if 1 <= abs(step) <= 3:
            return 1

    if len(line) < 2:
        return 0

    initial_step = line[1] - line[0]

    if not is_valid_step_size(initial_step):
        return 0

    trend = 1 if initial_step > 0 else -1

    for curr, next in zip(line, line[1:]):
        step = next - curr

        if not is_valid_step_size(step):
            return 0

        if step > 0 and trend < 0 or step < 0 and trend > 0:
            return 0

    return 1


# Entry point
if __name__ == "__main__":
    main()
