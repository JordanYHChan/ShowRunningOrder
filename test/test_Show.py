from src.Show import Show

dance_names = ["Jazz", "Contemporary", "Ballet"]
dancers_per_dance = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve", "Frank"],
    ["Grace", "Hannah", "Ivy"],
]


def test_Show():
    show = Show(dance_names, dancers_per_dance)
    assert len(show) == 3
    assert (
        str(show)
        == "Jazz: Alice, Bob, Charlie\nContemporary: David, Eve, Frank\nBallet: Grace, Hannah, Ivy"
    )
    assert [str(dance) for dance in show] == [
        "Jazz: Alice, Bob, Charlie",
        "Contemporary: David, Eve, Frank",
        "Ballet: Grace, Hannah, Ivy",
    ]
    assert show[0].name == "Jazz"
    assert show[0][0] == "Alice"
    assert len(show[0]) == 3
    assert [dancer for dancer in show[0]] == ["Alice", "Bob", "Charlie"]
