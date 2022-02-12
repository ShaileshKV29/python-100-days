from audioop import add
from unicodedata import name


def calculate(**kwargs):
    print(kwargs)

calculate(add=4,name="Shailesh")

def calculate2(n, **kwargs):
    print(n)
    n = kwargs["home"]
    print(kwargs)

calculate2(2, name="Key", value="Nothing")