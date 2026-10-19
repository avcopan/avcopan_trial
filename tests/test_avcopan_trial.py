"""avcopan_trial tests."""

import avcopan_trial


def test_stub() -> None:
    """Stub test to ensure the test suite runs."""
    print(avcopan_trial.__version__)  # noqa: T201


def test__greet() -> None:
    """Test the greet function."""
    assert avcopan_trial.greet("World") == "Hello, World!"


def test__greet_jim() -> None:
    """Test the greet_jim function."""
    assert avcopan_trial.greet_jim() == "Hello, Jim!"
