from typing import List

class Type():
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @property
    def weak(self):
        return self._weak

    @weak.setter
    def weak(self, value: List):
        self._weak = value

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, value: List):
        self._resistance = value

    @property
    def immune(self):
        return self._immune

    @immune.setter
    def immune(self, value: List):
        self._immune = value

    @property
    def double(self):
        return self._double

    @double.setter
    def double(self, value: List):
        self._double = value

    @property
    def half(self):
        return self._half

    @half.setter
    def half(self, value: List):
        self._half = value

    @property
    def zero(self):
        return self._zero

    @zero.setter
    def zero(self, value: List):
        self._zero = value


class Pokemon():
    def __init__(self, types: List):
        self.types      = types
        self.weak       = []
        self.resistance = []
        self.immune     = []
        self.double     = []
        self.half       = []
        self.zero       = []

        for type in self.types:
            self.weak.extend(type.weak)
            self.resistance.extend(type.resistance)
            self.immune.extend(type.immune)
            self.double.extend(type.double)
            self.half.extend(type.half)
            self.zero.extend(type.zero)

        self.weak       = list(set(self.weak))
        self.resistance = list(set(self.resistance))
        self.immune     = list(set(self.immune))
        self.double     = list(set(self.double))
        self.half       = list(set(self.half))
        self.zero       = list(set(self.zero))

    @property
    def weak(self):
        return self._weak

    @property
    def resistance(self):
        return self._resistance

    @property
    def immune(self):
        return self._immune

    @property
    def double(self):
        return self._double

    @property
    def half(self):
        return self._half

    @property
    def zero(self):
        return self._zero


class Team():
    def __init__(self, pokemon_lst: List):
        self.pokemon_lst = pokemon_lst
        self.weak       = []
        self.resistance = []
        self.immune     = []
        self.double     = []
        self.half       = []
        self.zero       = []

        for pokemon in self.pokemon_lst:
            self.weak.extend(pokemon.weak)
            self.resistance.extend(pokemon.resistance)
            self.immune.extend(pokemon.immune)
            self.double.extend(pokemon.double)
            self.half.extend(pokemon.half)
            self.zero.extend(pokemon.zero)

        self.weak       = list(set(self.weak))
        self.resistance = list(set(self.resistance))
        self.immune     = list(set(self.immune))
        self.double     = list(set(self.double))
        self.half       = list(set(self.half))
        self.zero       = list(set(self.zero))