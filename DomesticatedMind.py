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


class HeadWithShoulders(USD):

    def __init__(self, **kwargs):
        file_path = "/Users/davidrug/Library/Mobile Documents/iCloud~md~obsidian/Documents/InterBrain/DomesticatedMind/HeadWithShoulders/HeadWithShoulders.usdz"
        fill_color = BLACK
        outline_only = True
        super().__init__(file_path=file_path, fill_color=fill_color, outline_only=outline_only, **kwargs)


class DomesticatedMind3D(CustomObject):

    def specify_parts(self):
        self.cube = FoldableCube(y=3, z=33, p=PI/2, color=BLUE, diameter=200, bottom=False)
        self.head = HeadWithShoulders(scale=2.8, y=-70, z=7)
        self.parts += [self.cube, self.head]

    def specify_creation(self):
        creation_action = XAction(
            Movement(self.cube.creation_parameter, (0, 1), part=self.cube),
            Movement(self.head.creation_parameter, (0, 1), part=self.head),
            target=self, completion_parameter=self.creation_parameter, name="Creation")


domesticated_mid = DomesticatedMind3D(creation=True)