from typing_extensions import Self


class Monad:

    def __init__(self, value): # Abstract more usefull values here
        self._value = value


    def apply(self, func: function) -> Self:
        # Abstract pipeline implementation here
        value = func(self._value)
        return Monad(value)