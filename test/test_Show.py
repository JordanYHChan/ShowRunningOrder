from src.Show import Show, Dance

dance_names = ["Ballet", "Contemporary", "Modern Ballet"]
dancers_per_dance = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve", "Frank"],
    ["Alice", "Grace", "Hannah"],
]
dance_styles = ["Ballet", None, "Ballet"]


def test_Show():
    global show
    show = Show(dance_names, dancers_per_dance, dance_styles)
    assert len(show) == 3
    assert str(show) == "Ballet, Contemporary, Modern Ballet"
    assert [str(dance) for dance in show] == [
        "Ballet: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Modern Ballet: Alice, Grace, Hannah",
    ]
    assert show["Ballet"].name == "Ballet"
    assert show["Ballet"].dancers == ["Alice", "Bob", "Charlie"]
    assert show["Ballet"][0] == "Alice"
    assert len(show["Ballet"]) == 3
    assert show["Ballet"].style == "Ballet"
    assert [dancer for dancer in show["Ballet"]] == ["Alice", "Bob", "Charlie"]
    assert show.number_of_dances == 3
    assert show.running_order == [None, None, None]
    assert show.cost_matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_calc_common_dancers():
    global show
    assert show.calc_common_dancers(show["Ballet"], show["Ballet"]) == 3
    assert show.calc_common_dancers(show["Ballet"], show["Contemporary"]) == 0
    assert show.calc_common_dancers(show["Ballet"], show["Modern Ballet"]) == 1
    assert show.calc_common_dancers(show["Contemporary"], show["Ballet"]) == 0
    assert show.calc_common_dancers(show["Contemporary"], show["Contemporary"]) == 3
    assert show.calc_common_dancers(show["Contemporary"], show["Modern Ballet"]) == 0
    assert show.calc_common_dancers(show["Modern Ballet"], show["Ballet"]) == 1
    assert show.calc_common_dancers(show["Modern Ballet"], show["Contemporary"]) == 0
    assert show.calc_common_dancers(show["Modern Ballet"], show["Modern Ballet"]) == 3


def test_Show_calc_common_styles():
    global show
    assert show.calc_common_styles(show["Ballet"], show["Ballet"]) == 1
    assert show.calc_common_styles(show["Ballet"], show["Contemporary"]) == 0
    assert show.calc_common_styles(show["Ballet"], show["Modern Ballet"]) == 1
    assert show.calc_common_styles(show["Contemporary"], show["Ballet"]) == 0
    assert show.calc_common_styles(show["Contemporary"], show["Contemporary"]) == 0
    assert show.calc_common_styles(show["Contemporary"], show["Modern Ballet"]) == 0
    assert show.calc_common_styles(show["Modern Ballet"], show["Ballet"]) == 1
    assert show.calc_common_styles(show["Modern Ballet"], show["Contemporary"]) == 0
    assert show.calc_common_styles(show["Modern Ballet"], show["Modern Ballet"]) == 1


def test_Show_calc_cost():
    global show
    assert show.calc_cost(show["Ballet"], show["Ballet"]) == 1_000_000
    assert show.calc_cost(show["Ballet"], show["Contemporary"]) == 0
    assert show.calc_cost(show["Ballet"], show["Modern Ballet"]) == 2
    assert show.calc_cost(show["Contemporary"], show["Ballet"]) == 0
    assert show.calc_cost(show["Contemporary"], show["Contemporary"]) == 1_000_000
    assert show.calc_cost(show["Contemporary"], show["Modern Ballet"]) == 0
    assert show.calc_cost(show["Modern Ballet"], show["Ballet"]) == 2
    assert show.calc_cost(show["Modern Ballet"], show["Contemporary"]) == 0
    assert show.calc_cost(show["Modern Ballet"], show["Modern Ballet"]) == 1_000_000


def test_Show_calc_cost_matrix():
    global show
    show.calc_cost_matrix()
    assert show.cost_matrix == [[1_000_000, 0, 2], [0, 1_000_000, 0], [2, 0, 1_000_000]]
    show.cost_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_set_position():
    global show
    assert show.running_order == [None, None, None]
    show.set_position(0, "Ballet")
    assert show.running_order == ["Ballet", None, None]
    show.set_position(1, "Contemporary")
    assert show.running_order == ["Ballet", "Contemporary", None]
    show.set_position(2, "Modern Ballet")
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet"]
    show.set_position(0, "Modern Ballet")
    assert show.running_order == ["Modern Ballet", "Contemporary", None]
    show.set_position(0, "Contemporary")
    assert show.running_order == ["Contemporary", None, None]
    show.set_position(0, None)
    assert show.running_order == [None, None, None]


def test_Show_is_possible():
    global show
    assert show.is_possible(0, show["Ballet"]) is True
    assert show.is_possible(1, show["Ballet"]) is True
    assert show.is_possible(2, show["Ballet"]) is True
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is True
    assert show.is_possible(1, show["Modern Ballet"]) is True
    assert show.is_possible(2, show["Modern Ballet"]) is True
    show.running_order = ["Ballet", None, None]
    assert show.is_possible(0, show["Ballet"]) is True
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is True
    show.running_order = [None, "Ballet", None]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is True
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is True
    show.running_order = [None, None, "Ballet"]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is True
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is True
    show.running_order = ["Ballet", None, None]
    show.calc_cost_matrix()
    assert show.is_possible(0, show["Ballet"]) is True
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is True
    assert show.is_possible(1, show["Modern Ballet"]) is False
    assert show.is_possible(2, show["Modern Ballet"]) is True
    show.running_order = [None, "Ballet", None]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is True
    assert show.is_possible(2, show["Ballet"]) is False
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is False
    assert show.is_possible(1, show["Modern Ballet"]) is True
    assert show.is_possible(2, show["Modern Ballet"]) is False
    show.running_order = [None, None, "Ballet"]
    assert show.is_possible(0, show["Ballet"]) is False
    assert show.is_possible(1, show["Ballet"]) is False
    assert show.is_possible(2, show["Ballet"]) is True
    assert show.is_possible(0, show["Contemporary"]) is True
    assert show.is_possible(1, show["Contemporary"]) is True
    assert show.is_possible(2, show["Contemporary"]) is True
    assert show.is_possible(0, show["Modern Ballet"]) is True
    assert show.is_possible(1, show["Modern Ballet"]) is False
    assert show.is_possible(2, show["Modern Ballet"]) is True
    show.running_order = [None, None, None]
    show.cost_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_order():
    global show
    assert show.order_dances() is True
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet"]
    show.running_order = [None, None, None]
    assert show.order_dances(0) is True
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet"]
    show.running_order = [None, None, None]
    assert show.order_dances(1) is True
    assert show.running_order == ["Modern Ballet", "Ballet", "Contemporary"]
    show.running_order = [None, None, None]
    assert show.order_dances(2) is True
    assert show.running_order == ["Contemporary", "Modern Ballet", "Ballet"]
    show.running_order = [None, None, None]
    show.calc_cost_matrix()
    assert show.cost_matrix == [[1_000_000, 0, 2], [0, 1_000_000, 0], [2, 0, 1_000_000]]
    assert show.order_dances() is True
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet"]
    show.running_order = [None, None, None]
    assert show.order_dances(0) is True
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet"]
    show.running_order = [None, None, None]
    assert show.order_dances(1) is True
    assert show.running_order == ["Modern Ballet", "Contemporary", "Ballet"]
    show.running_order = [None, None, None]
    assert show.order_dances(2) is True
    assert show.running_order == ["Modern Ballet", "Contemporary", "Ballet"]
    show.running_order = [None, "Contemporary", None]
    assert show.order_dances() is True
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet"]
    show.running_order = [None, "Contemporary", None]
    assert show.order_dances(1) is True
    assert show.running_order == ["Modern Ballet", "Contemporary", "Ballet"]
    show.running_order = [None, "Contemporary", None]
    assert show.order_dances(2) is True
    assert show.running_order == ["Modern Ballet", "Contemporary", "Ballet"]
    show.running_order = [None, "Ballet", None]
    assert show.order_dances() is False
    assert show.running_order == [None, "Ballet", None]
    show.running_order = [None, "Modern Ballet", None]
    assert show.order_dances() is False
    assert show.running_order == [None, "Modern Ballet", None]
    show.running_order = ["Contemporary", None, None]
    assert show.order_dances() is False
    assert show.running_order == ["Contemporary", None, None]
    show.running_order = [None, None, "Contemporary"]
    assert show.order_dances() is False
    assert show.running_order == [None, None, "Contemporary"]
    show.running_order = [None, None, None]
    show.cost_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_add_dance():
    global show
    show.add_dance(Dance("Tap", ["Bob", "Charlie", "Ivy"]))
    assert str(show) == "Ballet, Contemporary, Modern Ballet, Tap"
    assert len(show) == 4
    assert [str(dance) for dance in show] == [
        "Ballet: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Modern Ballet: Alice, Grace, Hannah",
        "Tap: Bob, Charlie, Ivy",
    ]
    assert show["Tap"].name == "Tap"
    assert show["Tap"].dancers == ["Bob", "Charlie", "Ivy"]
    assert show["Tap"][0] == "Bob"
    assert len(show["Tap"]) == 3
    assert show["Tap"].style is None
    assert [dancer for dancer in show["Tap"]] == ["Bob", "Charlie", "Ivy"]
    assert show.number_of_dances == 4
    assert show.running_order == [None, None, None, None]
    assert show.cost_matrix == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    show.calc_cost_matrix()
    assert show.cost_matrix == [
        [1_000_000, 0, 2, 2],
        [0, 1_000_000, 0, 0],
        [2, 0, 1_000_000, 0],
        [2, 0, 0, 1_000_000],
    ]
    assert show.order_dances() is True
    assert show.running_order == ["Ballet", "Contemporary", "Modern Ballet", "Tap"]
    show.add_dance(Dance("Hip Hop", ["Bob", "David", "Ivy"], "Hip Hop"))
    assert str(show) == "Ballet, Contemporary, Hip Hop, Modern Ballet, Tap"
    assert len(show) == 5
    assert [str(dance) for dance in show] == [
        "Ballet: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Hip Hop: Bob, David, Ivy",
        "Modern Ballet: Alice, Grace, Hannah",
        "Tap: Bob, Charlie, Ivy",
    ]
    assert show["Hip Hop"].name == "Hip Hop"
    assert show["Hip Hop"].dancers == ["Bob", "David", "Ivy"]
    assert show["Hip Hop"][0] == "Bob"
    assert len(show["Hip Hop"]) == 3
    assert show["Hip Hop"].style == "Hip Hop"
    assert [dancer for dancer in show["Hip Hop"]] == ["Bob", "David", "Ivy"]
    assert show.number_of_dances == 5
    assert show.running_order == [
        "Ballet",
        "Contemporary",
        "Modern Ballet",
        "Tap",
        None,
    ]
    assert show.cost_matrix == [
        [1_000_000, 0, 0, 2, 2],
        [0, 1_000_000, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [2, 0, 0, 1_000_000, 0],
        [2, 0, 0, 0, 1_000_000],
    ]
    show.calc_cost_matrix()
    assert show.cost_matrix == [
        [1_000_000, 0, 1, 2, 2],
        [0, 1_000_000, 1, 0, 0],
        [1, 1, 1_000_000, 0, 2],
        [2, 0, 0, 1_000_000, 0],
        [2, 0, 2, 0, 1_000_000],
    ]
    assert show.order_dances() is False
    show.running_order = [None, None, None, None, None]
    assert show.order_dances() is True
    assert show.running_order == [
        "Ballet",
        "Contemporary",
        "Tap",
        "Modern Ballet",
        "Hip Hop",
    ]
    show.running_order = [None, None, None, None, None]
    show.cost_matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_Show_add_intermission():
    show.add_intermission()
    assert (
        str(show) == "Ballet, Contemporary, Hip Hop, Intermission, Modern Ballet, Tap"
    )
    assert len(show) == 6
    assert [str(dance) for dance in show] == [
        "Ballet: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Hip Hop: Bob, David, Ivy",
        "Intermission: ",
        "Modern Ballet: Alice, Grace, Hannah",
        "Tap: Bob, Charlie, Ivy",
    ]
    assert show["Intermission"].name == "Intermission"
    assert show["Intermission"].dancers == []
    assert len(show["Intermission"]) == 0
    assert [dancer for dancer in show["Intermission"]] == []
    assert show.number_of_dances == 6
    assert show.running_order == [None, None, None, "Intermission", None, None]
    assert show.cost_matrix == [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    show.calc_cost_matrix()
    assert show.cost_matrix == [
        [1_000_000, 0, 1, 0, 2, 2],
        [0, 1_000_000, 1, 0, 0, 0],
        [1, 1, 1_000_000, 0, 0, 2],
        [0, 0, 0, 1_000_000, 0, 0],
        [2, 0, 0, 0, 1_000_000, 0],
        [2, 0, 2, 0, 0, 1_000_000],
    ]
    assert show.order_dances() is True
    assert show.running_order == [
        "Ballet",
        "Contemporary",
        "Tap",
        "Intermission",
        "Hip Hop",
        "Modern Ballet",
    ]
