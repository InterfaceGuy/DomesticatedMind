import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *


class DomesticatedMind(CustomObject):

    def specify_parts(self):
        self.cube = FoldableCube(y=3, z=33, p=PI/2, color=BLUE, diameter=200, bottom=False)
        self.head = Human(y=-10, filled=True, fill_color=BLACK)
        self.parts += [self.cube, self.head]

    def specify_creation(self):
        creation_action = XAction(
            Movement(self.cube.creation_parameter, (1/3, 1), part=self.cube),
            Movement(self.head.creation_parameter, (0, 2/3), part=self.head),
            target=self, completion_parameter=self.creation_parameter, name="Creation")