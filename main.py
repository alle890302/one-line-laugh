import os

LINE = "I meal-prep on Sundays so by Wednesday I can feel guilty about five containers at once instead of one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
