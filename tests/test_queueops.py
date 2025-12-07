from src.queueops import take_next, move_to_back, interleave


def test_take_next():
    assert take_next([]) == (None, [])
    assert take_next(["ann"]) == ("ann", [])
    assert take_next(["ann", "bob"]) == ("ann", ["bob"])


def test_move_to_back():
    assert move_to_back(["ann", "bob", "cara"], "bob") == ["ann", "cara", "bob"]
    assert move_to_back(["ann"], "ann") == ["ann"]
    assert move_to_back(["ann", "bob"], "zoe") == ["ann", "bob"]


def test_interleave():
    assert interleave(["a", "b", "c"], ["x", "y"]) == ["a", "x", "b", "y", "c"]
    assert interleave([], ["x"]) == ["x"]
    assert interleave(["a"], []) == ["a"]