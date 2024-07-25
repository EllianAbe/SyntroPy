from typing import List


class Hamburguer:
    def __init__(self, bread: str, meat: List[str], cheese: List[str], toppings: List[str]):
        self.bread = bread
        self.meat = meat
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self) -> str:
        return f"Hamburguer with bread: {self.bread}, " \
               f"{len(self.meat)} meat(s): {', '.join(self.meat)}, " \
               f"{len(self.cheese)} cheese(s): {', '.join(self.cheese)}, " \
               f"toppings: {', '.join(self.toppings)}"


class HamburguerBuilder:
    def __init__(self):
        self.hamburguer = Hamburguer("", [], [], [])

    def add_bread(self, bread: str) -> "HamburguerBuilder":
        self.hamburguer.bread = bread
        return self

    def add_meat(self, meat: str) -> "HamburguerBuilder":
        self.hamburguer.meat.append(meat)
        return self

    def add_cheese(self, cheese: str) -> "HamburguerBuilder":
        self.hamburguer.cheese.append(cheese)
        return self

    def add_topping(self, topping: str) -> "HamburguerBuilder":
        self.hamburguer.toppings.append(topping)
        return self

    def build(self) -> Hamburguer:
        if not self.hamburguer.bread:
            raise ValueError("Bread is required to build a Hamburguer.")
        if not self.hamburguer.meat:
            raise ValueError("At least one type of meat is required.")
        return self.hamburguer


if __name__ == "__main__":
    hamburguer = (HamburguerBuilder()
                  .add_bread("wheat")
                  .add_meat("beef")
                  .add_cheese("swiss")
                  .add_meat("chicken")
                  .add_topping("ketchup")
                  .add_cheese("cheddar")
                  .add_topping("lettuce")).build()

    print(hamburguer)
