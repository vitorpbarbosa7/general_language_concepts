from typing import Dict, Type, Tuple, List, Union

class Ocean:
    '''
    Example of class not breaking the Demeter Law
    https://www.youtube.com/watch?v=FyJhALHmFXU
    '''

    def __init__(self, name):
        self.name = name

    @property
    def fishes(self):
        return self._name_condition

    @fishes.setter
    def fishes(self, name_condition:Dict):
        self._name_condition = name_condition

    def hungry_fishes(self):
        try:
            return [key for key, value in self.fishes.items() if value == 1]
        except Exception as e:
            print(e)


if __name__ == '__main__':
    atlantico = Ocean('atlantico')
    print(atlantico.hungry_fishes())
    atlantico.fishes = {'a':1,'b':0}
    print(atlantico.fishes)
    print(atlantico.hungry_fishes())