import pytest
import unittest.mock as mock

from src.controllers.receipecontroller import ReceipeController #doesnt work,
# tried using ...src.controllers.receipecontroller but that doesnt work either.

## I didnt get the pathing to work so im not 100% sure that the code below is working correctly since I couldnt test it.

#Readiness over 0.1, correct diet
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

##readiness 0 (under 0.1), correct diet
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

#Tries giving a recipe not for vegetarians to a vegetarian
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