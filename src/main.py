import sys
from Show import read, write, Show

if __name__ == "__main__":
    # get the input and output file location from the user
    input_file = (
        sys.argv[1] if len(sys.argv) > 1 else input("Enter the input file location: ")
    )
    output_file = (
        sys.argv[2] if len(sys.argv) > 2 else input("Enter the output file location: ")
    )

    # read the input file
    dance_names, dancers_per_dance, dance_styles = read(input_file)

    # create a Show object with an intermission
    show = Show(dance_names, dancers_per_dance, dance_styles)
    print(show)
    show.add_intermission()

    # check if the user wants to position certain dances
    while True:
        dance_name = input("Enter the dance name to position (or 'done'): ")
        if dance_name == "done":
            break
        if dance_name not in dance_names:
            print("Invalid dance name")
            continue
        position = input("Enter the position to place the dance: ")
        if (
            position == "first"
            or position == "start"
            or position == "beginning"
            or position == "opening"
        ):
            position = 0
        elif (
            position == "last"
            or position == "final"
            or position == "end"
            or position == "closing"
        ):
            position = show.number_of_dances - 1
        elif position == "before intermission":
            position = show.running_order.index("Intermission") - 1
        elif position == "after intermission":
            position = show.running_order.index("Intermission") + 1
        elif position.isdigit():
            position = int(position)
        else:
            print("Invalid position")
            continue
        show.set_position(position, dance_name)

    # order the dances
    show.calc_cost_matrix()
    show.order_dances()
    print(show)

    # write the output file
    write(output_file, show)
