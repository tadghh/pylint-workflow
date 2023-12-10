from fruit_types import Fruit


class Fruit_Object:
    def __init__(self, fruit_type):
        print("a")
        self.fruit_type = fruit_type

    def decompose(self):
        "The fruit succumbs to the elements."
        try:
            if not isinstance(self.fruit_type, Fruit):
                raise ValueError(
                    "Lets hope this can decompose. Added %s to the community compost."
                    % self.fruit_type
                )

            print("The soil absorbs the nutrients from %s", self.fruit_type)
            return None
        except Exception as error:
            print("error: %s", error)
