from src.Show import Show

dance_names = ["Ballet", "Contemporary", "Jazz"]
dancers_per_dance = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve", "Frank"],
    ["Alice", "Grace", "Hannah"],
]


def test_Show():
    global show
    show = Show(dance_names, dancers_per_dance)
    assert len(show) == 3
    assert (
        str(show)
        == "Ballet: Alice, Bob, Charlie\nContemporary: David, Eve, Frank\nJazz: Alice, Grace, Hannah"
    )
    assert [str(dance) for dance in show] == [
        "Ballet: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Jazz: Alice, Grace, Hannah",
    ]
    assert show["Ballet"].name == "Ballet"
    assert show["Ballet"].dancers == ["Alice", "Bob", "Charlie"]
    assert show["Ballet"][0] == "Alice"
    assert len(show["Ballet"]) == 3
    assert [dancer for dancer in show["Ballet"]] == ["Alice", "Bob", "Charlie"]
    assert show.number_of_dances == 3
    assert show.running_order == [None, None, None]
    assert show.cost_matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_calc_common_dancers():
    global show
    assert show.calc_common_dancers(show["Ballet"], show["Ballet"]) == 3
    assert show.calc_common_dancers(show["Ballet"], show["Contemporary"]) == 0
    assert show.calc_common_dancers(show["Ballet"], show["Jazz"]) == 1
    assert show.calc_common_dancers(show["Contemporary"], show["Ballet"]) == 0
    assert show.calc_common_dancers(show["Contemporary"], show["Contemporary"]) == 3
    assert show.calc_common_dancers(show["Contemporary"], show["Jazz"]) == 0
    assert show.calc_common_dancers(show["Jazz"], show["Ballet"]) == 1
    assert show.calc_common_dancers(show["Jazz"], show["Contemporary"]) == 0
    assert show.calc_common_dancers(show["Jazz"], show["Jazz"]) == 3


def test_Show_calc_cost():
    global show
    assert show.calc_cost(show["Ballet"], show["Ballet"]) == 1_000_000
    assert show.calc_cost(show["Ballet"], show["Contemporary"]) == 0
    assert show.calc_cost(show["Ballet"], show["Jazz"]) == 1
    assert show.calc_cost(show["Contemporary"], show["Ballet"]) == 0
    assert show.calc_cost(show["Contemporary"], show["Contemporary"]) == 1_000_000
    assert show.calc_cost(show["Contemporary"], show["Jazz"]) == 0
    assert show.calc_cost(show["Jazz"], show["Ballet"]) == 1
    assert show.calc_cost(show["Jazz"], show["Contemporary"]) == 0
    assert show.calc_cost(show["Jazz"], show["Jazz"]) == 1_000_000


def test_Show_calc_cost_matrix():
    global show
    show.calc_cost_matrix()
    assert show.cost_matrix == [[1_000_000, 0, 1], [0, 1_000_000, 0], [1, 0, 1_000_000]]
    show.cost_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_is_possible():
    global show
    assert show.is_possible(0, show["Ballet"]) is True
    assert show.is_possible(1, show["Ballet"]) is True
    assert show.is_possible(2, show["Ballet"]) is True
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is True
    show.running_order = ["Ballet", None, None]
    assert show.is_possible(0, show["Ballet"]) is True
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is True
    show.running_order = [None, "Ballet", None]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is True
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is True
    show.running_order = [None, None, "Ballet"]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is True
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is True
    show.running_order = ["Ballet", None, None]
    show.calc_cost_matrix()
    assert show.is_possible(0, show["Ballet"]) is True
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is True
    assert show.is_possible(1, show["Jazz"]) is False
    assert show.is_possible(2, show["Jazz"]) is True
    show.running_order = [None, "Ballet", None]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is True
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is False
    assert show.is_possible(1, show["Jazz"]) is True
    assert show.is_possible(2, show["Jazz"]) is False
    show.running_order = [None, None, "Ballet"]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is True
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Jazz"]) is True
    assert show.is_possible(1, show["Jazz"]) is False
    assert show.is_possible(2, show["Jazz"]) is True
    show.running_order = [None, None, None]
    show.cost_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
