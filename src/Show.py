def read(input_file):
    with open(input_file, "r") as file:
        dance_names = file.readline().strip().split(sep=", ")
        number_of_dances = len(dance_names)
        dancers_per_dance = [
            file.readline().strip().split(sep=", ") for _ in range(number_of_dances)
        ]
    return dance_names, dancers_per_dance


def write(output_file, show):
    with open(output_file, "w") as file:
        file.write(str(show))
    pass


class Dance:
    def __init__(self, name, dancers):
        self.name = name
        self.dancers = sorted(dancers)
        self.dancers_set = set(self.dancers)

    def __str__(self):
        return f"{self.name}: {', '.join(self.dancers)}"

    def __getitem__(self, key):
        return self.dancers[key]

    def __len__(self):
        return len(self.dancers)

    def __iter__(self):
        return iter(self.dancers)


class Show:
    def __init__(self, dance_names, dancers_per_dance):
        self.dances = [
            Dance(dance_name, dancers)
            for dance_name, dancers in zip(dance_names, dancers_per_dance)
        ]
        self.dances.sort(key=lambda dance: dance.name)
        self.number_of_dances = len(dance_names)
        self.running_order = [None] * self.number_of_dances
        self.cost_matrix = [
            [0] * self.number_of_dances for _ in range(self.number_of_dances)
        ]

    def is_possible(self, pos, dance):
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

    def calc_common_dancers(self, dance1, dance2):
        return len(dance1.dancers_set & dance2.dancers_set)

    def calc_cost(self, dance1, dance2):
        if dance1 == dance2:
            return 1_000_000
        cost = 0
        cost += self.calc_common_dancers(dance1, dance2)
        return cost

    def calc_cost_matrix(self):
        for i, dance1 in enumerate(self.dances):
            for j, dance2 in enumerate(self.dances):
                self.cost_matrix[i][j] = self.calc_cost(dance1, dance2)
        pass

    def order_dances(self, pos=None):
        if None not in self.running_order:
            return True
        if not pos or pos > self.number_of_dances - 1:
            pos = 0
        if self.running_order[pos]:
            return self.order_dances(pos + 1)
        for dance in self.dances:
            if self.is_possible(pos, dance):
                self.running_order[pos] = dance.name
                if self.order_dances(pos + 1):
                    return True
            self.running_order[pos] = None
        return False

    def add_dance(self, dance):
        self.dances.append(dance)
        self.dances.sort(key=lambda dance: dance.name)
        self.number_of_dances += 1
        self.running_order.append(None)
        index = self.dances.index(dance)
        for row in self.cost_matrix:
            row.insert(index, 0)
        self.cost_matrix.insert(index, [0] * self.number_of_dances)

    def add_intermission(self):
        self.add_dance(Dance("Intermission", []))
        self.running_order[self.number_of_dances // 2] = "Intermission"

    def __str__(self):
        if all(self.running_order):
            return ", ".join(
                [dance.name for dance in [self[dance] for dance in self.running_order]]
            )
        return ", ".join([dance.name for dance in self.dances])

    def __getitem__(self, key):
        index = [dance.name for dance in self.dances].index(key)
        return self.dances[index]

    def __len__(self):
        return len(self.dances)

    def __iter__(self):
        return iter(self.dances)
