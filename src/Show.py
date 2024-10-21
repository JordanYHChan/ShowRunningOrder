def read(input_file):
    """
    Read the input file and return the data as a tuple of dance names, dancers per dance and dance styles.

    Parameters:
    input_file (str): The path to the input file.

    Returns:
    tuple: A tuple of dance names, dancers per dance and dance styles.
    """
    with open(input_file, "r") as file:
        dance_names = file.readline().strip().split(sep=", ")
        number_of_dances = len(dance_names)
        dancers_per_dance = [
            file.readline().strip().split(sep=", ") for _ in range(number_of_dances)
        ]
        dance_styles = file.readline().strip().split(sep=", ")
    return dance_names, dancers_per_dance, dance_styles


def write(output_file, show):
    """
    Write the show to the output file.

    Parameters:
    output_file (str): The path to the output file.
    show (Show): The show to write to the output file.
    """
    with open(output_file, "w") as file:
        file.write(str(show))


class Dance:
    def __init__(self, name, dancers, style=None):
        """
        Create a dance object.

        Parameters:
        name (str): The name of the dance.
        dancers (list): A list of the dancers in the dance.
        style (str): The style of the dance. Default is None.

        Attributes:
        name (str): The name of the dance.
        style (str): The style of the dance.
        dancers (list): A list of the dancers in the dance in alphabetical order.
        dancers_set (set): A set of the dancers in the dance.

        Methods:
        __str__(): Return the string representation of the dance.
        __getitem__(key): Return the dancer at the given index.
        __len__(): Return the number of dancers in the dance.
        __iter__(): Return an iterator over the dancers in the dance.
        """
        self.name = name
        self.style = style
        self.dancers = sorted(dancers)
        self.dancers_set = set(self.dancers)

    def __str__(self):
        """
        Return the string representation of the dance in the format "name: dancer1, dancer2, ...".

        Returns:
        str: The string representation of the dance.
        """
        return f"{self.name}: {', '.join(self.dancers)}"

    def __getitem__(self, key):
        """
        Return the dancer at the given index in alphabetical order.

        Parameters:
        key (int): The index of the dancer.

        Returns:
        str: The dancer at the given index.
        """
        return self.dancers[key]

    def __len__(self):
        """
        Return the number of dancers in the dance.

        Returns:
        int: The number of dancers in the dance.
        """
        return len(self.dancers)

    def __iter__(self):
        """
        Return an iterator over the dancers in the dance.

        Returns:
        iter: An iterator over the dancers in the dance.
        """
        return iter(self.dancers)


class Show:
    def __init__(self, dance_names, dancers_per_dance, dance_styles=None):
        """
        Create a show object.

        Parameters:
        dance_names (list): A list of the names of the dances.
        dancers_per_dance (list): A list of the dancers in each dance.
        dance_styles (list): A list of the styles of the dances.

        Attributes:
        dances (list): A list of the dances in alphabetical order.
        number_of_dances (int): The number of dances in the show.
        running_order (list): A list of the names of the dances in the running order.
        common_dancers (bool): A flag indicating whether common dancers are considered. Default is True.
        common_styles (bool): A flag indicating whether common styles are considered. Default is True.
        cost_matrix (list): A matrix of the costs between the dances.
        neighbours (dict): A dictionary of the neighbours of each dance.

        Methods:
        set_common_dancers(common_dancers): Set the flag indicating whether common dancers are considered.
        set_common_styles(common_styles): Set the flag indicating whether common styles are considered.
        calc_common_dancers(dance1, dance2): Calculate the number of common dancers between two dances.
        calc_common_styles(dance1, dance2): Calculate the number of common styles between two dances.
        calc_cost(dance1, dance2): Calculate the cost between two dances.
        calc_cost_matrix(): Calculate the cost matrix between the dances.
        create_neighbours(): Create the neighbours of each dance.
        is_possible(pos, dance): Check if it is possible to place a dance at a given position.
        order_dances(pos=None): Order the dances in the running order.
        add_dance(dance): Add a dance to the show.
        add_intermission(): Add an intermission to the show.
        set_position(pos, dance_name): Set the position of a dance in the running order.
        __str__(): Return the string representation of the show.
        __getitem__(key): Return the dance with the given name.
        __len__(): Return the number of dances in the show.
        __iter__(): Return an iterator over the dances in the show.
        """
        if not dance_styles:
            dance_styles = [None] * len(dance_names)
        self.dances = [
            Dance(dance_name, dancers, dance_style)
            for dance_name, dancers, dance_style in zip(
                dance_names, dancers_per_dance, dance_styles
            )
        ]
        self.dances.sort(key=lambda dance: dance.name)
        self.number_of_dances = len(dance_names)
        self.running_order = [None] * self.number_of_dances
        self.common_dancers = True
        self.common_styles = True
        self.cost_matrix = [
            [0] * self.number_of_dances for _ in range(self.number_of_dances)
        ]

    def set_common_dancers(self, common_dancers):
        """
        Set the flag indicating whether common dancers are considered.

        Parameters:
        common_dancers (bool): A flag indicating whether common dancers are considered.
        """
        self.common_dancers = common_dancers

    def set_common_styles(self, common_styles):
        """
        Set the flag indicating whether common styles are considered.

        Parameters:
        common_styles (bool): A flag indicating whether common styles are considered.
        """
        self.common_styles = common_styles

    def calc_common_dancers(self, dance1, dance2):
        """
        Calculate the number of common dancers between two dances.

        Parameters:
        dance1 (Dance): The first dance.
        dance2 (Dance): The second dance.

        Returns:
        int: The number of common dancers between the two dances.
        """
        return len(dance1.dancers_set & dance2.dancers_set)

    def calc_common_styles(self, dance1, dance2):
        """
        Calculate the number of common styles between two dances.

        Parameters:
        dance1 (Dance): The first dance.
        dance2 (Dance): The second dance.

        Returns:
        int: The number of common styles between the two dances.
        """
        if dance1.style and dance2.style:
            return int(dance1.style == dance2.style)
        return 0

    def calc_cost(self, dance1, dance2):
        """
        Calculate the cost between two dances.

        The cost is calculated by summing the number of common dancers and the number of common styles between the two
        dances if the flags indicating whether common dancers and common styles are considered are set to True.

        Parameters:
        dance1 (Dance): The first dance.
        dance2 (Dance): The second dance.

        Returns:
        int: The cost between the two dances.
        """
        if dance1 == dance2:
            return 1_000_000
        cost = 0
        if self.common_dancers:
            cost += self.calc_common_dancers(dance1, dance2)
        if self.common_styles:
            cost += self.calc_common_styles(dance1, dance2)
        return cost

    def calc_cost_matrix(self):
        """
        Calculate the cost matrix between the dances.

        The cost matrix is a matrix of the costs between the dances.
        """
        for i, dance1 in enumerate(self.dances):
            for j, dance2 in enumerate(self.dances):
                self.cost_matrix[i][j] = self.calc_cost(dance1, dance2)

    def create_neighbours(self):
        """
        Create the neighbours of each dance.

        The neighbours of a dance are the dances that can be placed before or after it in the running order.
        """
        self.neighbours = {}
        for i, dance1 in enumerate(self.dances):
            self.neighbours[dance1.name] = []
            for j, dance2 in enumerate(self.dances):
                if self.cost_matrix[i][j] == 0:
                    self.neighbours[dance1.name].append(dance2.name)

    def is_possible(self, pos, dance):
        """
        Check if it is possible to place a dance at a given position in the running order.

        A dance is possible to place at a given position if it is not already in the running order, and it is not before
        or after another dance that it has a cost with.

        Parameters:
        pos (int): The position in the running order.
        dance (Dance): The dance to place.

        Returns:
        bool: True if the dance is possible to place at the given position, False otherwise.
        """
        if dance.name in self.running_order[:pos] + self.running_order[pos + 1 :]:
            return False
        if (
            pos > 0
            and self.running_order[pos - 1]
            and self.cost_matrix[self.dances.index(dance)][
                self.dances.index(self[self.running_order[pos - 1]])
            ]
            > 0
        ):
            return False
        if (
            pos < self.number_of_dances - 1
            and self.running_order[pos + 1]
            and self.cost_matrix[self.dances.index(dance)][
                self.dances.index(self[self.running_order[pos + 1]])
            ]
            > 0
        ):
            return False
        return True

    def order_dances(self, pos=None):
        """
        Order the dances in the running order.

        The dances are ordered in the running order by placing each dance at a position in the running order if it is
        possible to place it at that position. This is done recursively until all the dances are ordered in the running
        order or it is not possible to place a dance at a position.

        Parameters:
        pos (int): The position in the running order. Default is None.

        Returns:
        bool: True if the dances are ordered in the running order, False otherwise.
        """
        if None not in self.running_order:
            return True
        if not pos or pos > self.number_of_dances - 1:
            pos = 0
        if self.running_order[pos]:
            return self.order_dances(pos + 1)
        for dance in sorted(self.dances, key=lambda dance: len(dance), reverse=True):
            if self.is_possible(pos, dance):
                self.running_order[pos] = dance.name
                if self.order_dances(pos + 1):
                    return True
            self.running_order[pos] = None
        return False

    def add_dance(self, dance):
        """
        Add a dance to the show.

        Parameters:
        dance (Dance): The dance to add to the show.
        """
        self.dances.append(dance)
        self.dances.sort(key=lambda dance: dance.name)
        self.number_of_dances += 1
        self.running_order.append(None)
        index = self.dances.index(dance)
        for row in self.cost_matrix:
            row.insert(index, 0)
        self.cost_matrix.insert(index, [0] * self.number_of_dances)

    def add_intermission(self):
        """
        Add an intermission to the show.

        The intermission is added to the running order at the middle of the show.
        """
        self.add_dance(Dance("Intermission", []))
        self.running_order[self.number_of_dances // 2] = "Intermission"

    def set_position(self, pos, dance_name):
        """
        Set the position of a dance in the running order.

        Parameters:
        pos (int): The position in the running order.
        dance_name (str): The name of the dance.
        """
        if dance_name and dance_name in self.running_order:
            self.running_order[self.running_order.index(dance_name)] = None
        self.running_order[pos] = dance_name

    def __str__(self):
        """
        Return the string representation of the show in the format "running order" if all the dances are in the running
        order, or in the format "dances" in alphabetical order otherwise.

        Returns:
        str: The string representation of the show.
        """
        if all(self.running_order):
            return ", ".join(
                [dance.name for dance in [self[dance] for dance in self.running_order]]
            )
        return ", ".join([dance.name for dance in self.dances])

    def __getitem__(self, key):
        """
        Return the dance with the given name.

        Parameters:
        key (str): The name of the dance.

        Returns:
        Dance: The dance with the given name.
        """
        index = [dance.name for dance in self.dances].index(key)
        return self.dances[index]

    def __len__(self):
        """
        Return the number of dances in the show.

        Returns:
        int: The number of dances in the show.
        """
        return len(self.dances)

    def __iter__(self):
        """
        Return an iterator over the dances in the show.

        Returns:
        iter: An iterator over the dances in the show.
        """
        return iter(self.dances)
