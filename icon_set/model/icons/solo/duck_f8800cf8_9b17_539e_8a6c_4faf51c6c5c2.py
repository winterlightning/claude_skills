"""toy-duck: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8800cf8-9b17-539e-8a6c-4faf51c6c5c2'
SOURCE_PATH = 'pictographic-primitives/animals/duck_f8800cf8-9b17-539e-8a6c-4faf51c6c5c2.svg'
AUTHOR = 'gpt-6'


class ToyDuck(Solo48):
    icon_id = 'toy-duck'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('duck', 'rubber duck', 'toy', 'bath', 'bird', 'debug', 'yellow', 'play')

    def build(self):
        self.add_line('silhouette-1', (13, 22), (2, 20))
        self.add_line('silhouette-2', (2, 20), (2, 16))
        self.add_line('silhouette-3', (2, 16), (11, 12))
        self.add_arc('silhouette-4', (11, 12), (21, 2), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('silhouette-5', (21, 2), (31, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_line('silhouette-6', (31, 12), (28, 26))
        self.add_arc('silhouette-7', (28, 26), (46, 22), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('silhouette-8', (46, 22), (32, 46), radius_x=14, radius_y=24, sweep=True)
        self.add_line('silhouette-9', (32, 46), (16, 46))
        self.add_arc('silhouette-10', (16, 46), (8, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('silhouette-11', (8, 38), (13, 22), radius_x=17, radius_y=17, sweep=True)
        self.add_contour('silhouette', 'silhouette-1', 'silhouette-2', 'silhouette-3', 'silhouette-4', 'silhouette-5', 'silhouette-6', 'silhouette-7', 'silhouette-8', 'silhouette-9', 'silhouette-10', 'silhouette-11', closed=True)
        self.add_arc('wing-1', (21, 34), (35, 37), radius_x=14, radius_y=3, sweep=False)
        self.add_contour('wing', 'wing-1', closed=False)
        self.add_dot('eye', (21, 11))
