def read(input_file):
    with open(input_file, "r") as file:
        dance_names = file.readline().strip().split(sep=", ")
        number_of_dances = len(dance_names)
        dancers_per_dance = [
            file.readline().strip().split(sep=", ") for _ in range(number_of_dances)
        ]
    return dance_names, dancers_per_dance


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
        self.running_order_indices = [-1] * self.number_of_dances
        self.cost_matrix = [
            [0] * self.number_of_dances for _ in range(self.number_of_dances)
        ]

    def is_possible(self, i, dance):
        dance_to_check_index = self.dances.index(dance)
        if dance_to_check_index == i:
            return True
        if self.running_order_indices[i] != -1:
            return False
        if dance_to_check_index in self.running_order_indices:
            return False
        return True

    def calculate_costs(self):
        for i in range(self.number_of_dances):
            for j in range(self.number_of_dances):
                if i == j:
                    self.cost_matrix[i][j] = 1_000_000
                    continue
                self.cost_matrix[i][j] = len(
                    self.dances[i].dancers_set & self.dances[j].dancers_set
                )
        pass

    def __str__(self):
        return "\n".join([str(dance) for dance in self.dances])

    def __getitem__(self, key):
        return self.dances[key]

    def __len__(self):
        return len(self.dances)

    def __iter__(self):
        return iter(self.dances)
