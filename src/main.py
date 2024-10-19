import sys
from Show import read, write, Show

if __name__ == "__main__":
    # get the input file location from the user
    input_file = (
        sys.argv[1] if len(sys.argv) > 1 else input("Enter the input file location: ")
    )

    # read the input file
    dance_names, dancers_per_dance = read(input_file)

    # create a Show object with an intermission
    show = Show(dance_names, dancers_per_dance)
    show.add_intermission()

    # order the dances
    show.calc_cost_matrix()
    show.order_dances()

    # write the output file
    print(show)
    output_file = (
        sys.argv[2] if len(sys.argv) > 2 else input("Enter the output file location: ")
    )
    write(output_file, show)
