class Base:
    def __init__(self) -> None:
        pass

    def base_method(self):
        print("Base Class")

class Derived(Base):
    def __init__(self) -> None:
        super().__init__()

    def derived_method(self):
        print("Inside Derived Class")
        self.base_method()

derived = Derived()
derived.base_method()
derived.derived_method()