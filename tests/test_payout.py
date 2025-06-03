import pytest

from payout import init, process, result


def test_init():
    """Тест функции инициализации."""
    data = init()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0] == 0
