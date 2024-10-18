import sys
from Show import read, Show

if __name__ == "__main__":
    # get the input file location from the user
    input_file = (
        sys.argv[1] if len(sys.argv) > 1 else input("Enter the input file location: ")
    )

    # read the input file
    dance_names, dancers_per_dance = read(input_file)

    # create a Show object
    show = Show(dance_names, dancers_per_dance)
    show.add_intermission()

    # order the dances
    show.calc_cost_matrix()
    show.order_dances()
    print(show)
