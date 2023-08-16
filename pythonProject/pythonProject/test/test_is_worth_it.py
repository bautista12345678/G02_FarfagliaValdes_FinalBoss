import pytest
from src.source import Ship, Cargo, Cruise


def test_ship_is_worth_it_positivo():
    ship = Ship(draft=400, crew=10)
    assert ship.is_worth_it() == True

def test_ship_is_worth_it_negativo():
    ship = Ship(draft=10, crew=10)
    assert ship.is_worth_it() == False



def test_cargo_is_worth_it_high_quality_positivo():
    cargo = Cargo(draft=60, crew=10, extra=5, quality=1)
    assert cargo.is_worth_it() == True

def test_cargo_is_worth_it_low_quality_negativo():
    cargo = Cargo(draft=30, crew=10, extra=5, quality=0.25)
    assert cargo.is_worth_it() == False

def test_cargo_is_worth_it_no_quality_negativo():
    cargo = Cargo(draft=30, crew=10, extra=5, quality=0)
    assert cargo.is_worth_it() == False



def test_cruise_is_worth_it_negativo():
    cruise = Cruise(draft=40, crew=20, extra=10)
    assert cruise.is_worth_it() == False

def test_cruise_is_worth_it_positivo():
    cruise = Cruise(draft=500, crew=20, extra=10)
    assert cruise.is_worth_it() == True



if __name__ == "__main__":
    pytest.main()