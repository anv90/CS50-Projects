import pytest
import unittest
from classes import Player
from unittest.mock import patch
from unittest.mock import Mock
from project import generate_players, death_saves, save_outcome



playa = Player("A", 12, 13)

def test_generate_players():
    mockObject = Player
    mockObject.get = Mock(side_effect=[playa, EOFError("EOF")])
    assert(generate_players()) == [playa]

def test_save_outcome():
     mockObject = Player
     mockObject.heal = Mock(return_value=10)
     assert save_outcome(playa, 1) == False
     assert save_outcome(playa, 2) == 0


def test_death_saves(monkeypatch):
    response = iter(["1", "2", "11"])
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert death_saves(playa) == 0
    monkeypatch.setattr('builtins.input', lambda _: "11")
    assert death_saves(playa) == 3
    monkeypatch.setattr('builtins.input', lambda _: next(response))
    assert death_saves(playa) == 1



