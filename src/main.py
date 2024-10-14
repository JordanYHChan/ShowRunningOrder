if __name__ == "__main__":
    # get the input file location from the user
    input_file = input("Enter the input file location: ")

    # read the input file
    with open(input_file, "r") as file:
        dance_names = file.readline().strip().split(sep=", ")
        number_of_dances = len(dance_names)
        dancers = [
            file.readline().strip().split(sep=", ") for _ in range(number_of_dances)
        ]
