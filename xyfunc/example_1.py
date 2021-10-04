import pytest

class Fruit(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.cubed = False

    def slice(self):
        self.cubed = True


class FruitSalad(object):
    def __init__(self, *fruits) -> None:
        super().__init__()
        self.fruits = fruits
        self._slice()
        
    def _slice(self):
        for fruit in self.fruits:
            fruit.slice()


@pytest.fixture
def fruit_bowl():
    return [Fruit('apple'), Fruit('banana'), Fruit('mango')]

def test_fruits(fruit_bowl):
    bowl = FruitSalad(*fruit_bowl)

    assert all(fruit.cubed for fruit in bowl.fruits)