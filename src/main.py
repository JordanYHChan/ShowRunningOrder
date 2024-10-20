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

    # create a Show object
    show = Show(dance_names, dancers_per_dance, dance_styles)
    print(show)

    # check if the user wants to add an intermission
    while True:
        intermission = input("Do you want to add an intermission (yes/no)? ")
        if intermission == "yes":
            show.add_intermission()
            break
        if intermission == "no":
            break
        print("Invalid option")

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

    # check what the user wants to consider when ordering the dances
    while True:
        common_dancers = input("Consider common dancers (yes/no)? ")
        if common_dancers == "yes":
            break
        if common_dancers == "no":
            show.set_common_dancers(False)
            break
        print("Invalid option")

    while True:
        common_styles = input("Consider common styles (yes/no)? ")
        if common_styles == "yes":
            break
        if common_styles == "no":
            show.set_common_styles(False)
            break
        print("Invalid option")

    # order the dances
    show.calc_cost_matrix()
    show.order_dances()
    print(show)

    # write the output file
    write(output_file, show)
