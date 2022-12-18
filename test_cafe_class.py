import inspect

import pytest

from app import Cafe, Building

PARAMETERS = [
    "name,tables,seats_at_table",
    [
        pytest.param(
            "Dafi",
            5,
            4,
            id="Cafe with name Dafi, 5 tables and 4 seats at each table"
        ),
        pytest.param(
            "KFC",
            20,
            6,
            id="Cafe with name KFC, 20 tables and 6 seats at each table"
        ),
        pytest.param(
            "McDonald's",
            10,
            4,
            id="Cafe with name McDonald's, 10 tables and 4 seats at each table"
        )
    ]
]


def test_cafe_is_child():
    assert issubclass(Cafe, Building)


@pytest.mark.parametrize(*PARAMETERS)
def test_cafe_has_is_open_attribute(name, tables, seats_at_table):
    cafe = Cafe(name, tables, seats_at_table)

    assert cafe.is_open is False


@pytest.mark.parametrize(*PARAMETERS)
def test_client_capacity(name, tables, seats_at_table):
    cafe = Cafe(name, tables, seats_at_table)

    assert cafe.client_capacity == (tables * seats_at_table)


def test_is_open_not_implemented_in_cafe_init():
    assert "self.is_open" not in inspect.getsource(Cafe.__init__)


def test_is_open_is_not_building_class_attribute():
    assert hasattr(Building, "is_open") is False


def test_is_open_is_not_cafe_class_attribute():
    assert hasattr(Cafe, "is_open") is False
