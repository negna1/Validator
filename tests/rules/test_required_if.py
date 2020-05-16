from validator.rules import RequiredIf


def test_required_if_01():
    rule = RequiredIf("a")
    value_to_check = "abc"
    assert rule(value_to_check)

    rule = RequiredIf("a")
    value_to_check = ["a", "b", "c"]
    assert rule(value_to_check)


def test_required_if_02():
    rule = RequiredIf("a")
    value_to_check = ""
    assert not rule(value_to_check)

    rule = RequiredIf("a")
    value_to_check = []
    assert not rule(value_to_check)

    rule = RequiredIf("a")
    value_to_check = "bcd"
    assert not rule(value_to_check)

    rule = RequiredIf("a")
    value_to_check = ["b", "c", "d"]
    assert not rule(value_to_check)
