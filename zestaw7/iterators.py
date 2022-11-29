import itertools
import random

iterator01 = itertools.cycle(range(0, 2))
iteratorBladzenieprzypadkowe = iter(iter((lambda: random.choice(("N", "E", "S", "W"))), 0))
iteratordni = itertools.cycle(range(0, 7))
