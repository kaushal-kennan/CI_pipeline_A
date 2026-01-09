from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


# Function to call the fail the test
"""def test_more_hello2():
    assert "Namaste" == more_hello()"""


def test_more_goodbye():
    assert "bye" == more_goodbye()
