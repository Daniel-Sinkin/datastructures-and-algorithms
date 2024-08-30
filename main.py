def main() -> None:
    grid = [
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0],
    ]

    # 1 -> 2
    starting_node = (2, 2)
    y_s, x_s = starting_node
    starting_val = grid[y_s][x_s]
    new_val = 2

    print(
        f"Want to flood-fill {starting_val} -> {new_val} starting from {starting_node}"
    )


if __name__ == "__main__":
    main()
