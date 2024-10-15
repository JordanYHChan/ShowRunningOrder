from src.Show import Dance


def test_Dance():
    dance = Dance("Jazz", ["Alice", "Bob", "Charlie"])
    assert str(dance) == "Jazz: Alice, Bob, Charlie"
    assert dance[0] == "Alice"
    assert len(dance) == 3
    assert [dancer for dancer in dance] == ["Alice", "Bob", "Charlie"]
