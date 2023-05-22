import pytest
import unittest.mock as mock

from src.controllers.receipecontroller import ReceipeController #doesnt work
# add your test case implementation here

## I didnt get the pathing to work so im not 100% sure that the code below is working correctly since I couldnt test it.
@pytest.mark.unit
def test_readiness_Over():
    mockedcalculate_readiness = mock.MagicMock()
    mockedcalculate_readiness.return_value = 1

    recipe = {"diets": [
        "normal"
    ],}

    sut = ReceipeController(calculate_readiness=mockedcalculate_readiness)
    validationResult = sut.get_readiness_of_receipes(recipe, [], "normal")

    assert validationResult == 1

@pytest.mark.unit
def test_readiness_Under():
    mockedcalculate_readiness = mock.MagicMock()
    mockedcalculate_readiness.return_value = 0

    recipe = {"diets": [
        "normal"
    ],}

    sut = ReceipeController(calculate_readiness=mockedcalculate_readiness)
    validationResult = sut.get_readiness_of_receipes(recipe, [], "normal")

    assert validationResult == 1

@pytest.mark.unit
def test_Incorrect_diet():
    mockedcalculate_readiness = mock.MagicMock()
    mockedcalculate_readiness.return_value = 0

    recipe = {"diets": [
        "normal"
    ],}

    sut = ReceipeController(calculate_readiness=mockedcalculate_readiness)
    validationResult = sut.get_readiness_of_receipes(recipe, [], "vegetarian")

    assert validationResult == 1