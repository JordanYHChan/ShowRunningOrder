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
        self.dancers = dancers

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

    def __str__(self):
        return "\n".join([str(dance) for dance in self.dances])

    def __getitem__(self, key):
        return self.dances[key]

    def __len__(self):
        return len(self.dances)

    def __iter__(self):
        return iter(self.dances)
