def main():

    with open("day-4/input.txt", "r") as f:
        input = [list(line) for line in f.readlines()]

    count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            column_slice, row_slice, diagonal_slice_right, diagonal_slice_left = (
                sliceInput(input, i, j)
            )

            if isKeyword(column_slice):
                count += 1
            if isKeyword(row_slice):
                count += 1
            if isKeyword(diagonal_slice_right):
                count += 1
            if isKeyword(diagonal_slice_left):
                count += 1

    print(count)


def isKeyword(arry):
    word = "".join(arry)

    return word == "XMAS" or word == "SAMX"


def sliceInput(input, i, j):
    return (
        columnSlice(input, i, j),
        rowSlice(input, i, j),
        diagonalSliceRight(input, i, j),
        diagonalSliceLeft(input, i, j),
    )


def columnSlice(input, i, j):
    try:
        return [input[i][j] for i in range(i, i + 4)]
    except IndexError:
        return []


def rowSlice(input, i, j):
    try:
        return [input[i][j] for j in range(j, j + 4)]
    except IndexError:
        return []


def diagonalSliceRight(input, i, start):
    try:
        return [input[i + (j - start)][j] for j in range(start, start + 4)]
    except IndexError:
        return []


def diagonalSliceLeft(input, i, start):
    try:
        return [input[i - (j - start)][j] for j in range(start, start + 4)]
    except IndexError:
        return []


if __name__ == "__main__":
    main()
