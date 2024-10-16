from src.Show import Show

dance_names = ["Jazz", "Contemporary", "Ballet"]
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
        == "Jazz: Alice, Bob, Charlie\nContemporary: David, Eve, Frank\nBallet: Alice, Grace, Hannah"
    )
    assert [str(dance) for dance in show] == [
        "Jazz: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Ballet: Alice, Grace, Hannah",
    ]
    assert show[0].name == "Jazz"
    assert show[0][0] == "Alice"
    assert len(show[0]) == 3
    assert [dancer for dancer in show[0]] == ["Alice", "Bob", "Charlie"]
    assert show.number_of_dances == 3
    assert show.running_order_indices == [-1, -1, -1]
    assert show.cost_matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_Show_is_possible():
    global show
    assert show.is_possible(0, show[0]) is True
    assert show.is_possible(1, show[0]) is True
    assert show.is_possible(2, show[0]) is True
    assert show.is_possible(0, show[1]) is True
    assert show.is_possible(0, show[2]) is True
    show.running_order_indices = [0, -1, -1]
    assert show.is_possible(0, show[0]) is False
    assert show.is_possible(1, show[0]) is False
    assert show.is_possible(2, show[0]) is False
    assert show.is_possible(0, show[1]) is True
    assert show.is_possible(0, show[2]) is True
    show.running_order_indices = [-1, -1, -1]


def test_Show_calculate_costs():
    global show
    show.calculate_costs()
    assert show.cost_matrix == [[1_000_000, 0, 1], [0, 1_000_000, 0], [1, 0, 1_000_000]]
