from challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_validate_brakets_if_True():
    expected=True
    actual=validate_brackets('{}')

    assert expected==actual

def test_validate_brakets_if_True2():
    expected=True
    actual=validate_brackets('{{}{Code}[Fellows](())}')

    assert expected==actual

def test_validate_brakets_if_True2():
    expected=True
    actual=validate_brackets('{([])}')

    assert expected==actual

def test_validate_brakets_if_False():
    expected=False
    actual=validate_brackets('[({}]')

    assert expected==actual

def test_validate_brakets_if_False2():
    expected=False
    actual=validate_brackets('(](')

    assert expected==actual

def test_validate_brakets_if_False3():
    expected=False
    actual=validate_brackets('(')

    assert expected==actual
