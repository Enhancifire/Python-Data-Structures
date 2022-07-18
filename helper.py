"""
Helper script
Generates the files required for each problem
Used by copying into folder and running, then giving it input.
"""


def main():
    """Main function
    Creates the required boilerplate files"""

    print("Input the number of problems of:")
    r = int(input("Reinforcement: "))
    c = int(input("Creativity: "))
    p = int(input("Project: "))

    mod = int(input("Enter Module No: "))

    for i in range(1, r + c + p + 1):
        if i <= r:
            with open(f"{mod}.{i}-R.py", "w") as f:
                pass
        elif r < i <= r + c:
            with open(f"{mod}.{i}-C.py", "w") as f:
                pass
        else:
            with open(f"{mod}.{i}-P.py", "w") as f:
                pass


if __name__ == "__main__":
    main()
