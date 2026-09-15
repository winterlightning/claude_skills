# Complete geometry repair; parent preserved.
'Paired eyes moved inward by one unit. Diamond beak reduced to an open V so no cramped internal counter remains. VRECT_L bounds retained; symmetry about x=24 preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'

class ChickenFace(Solo48):
    icon_id = 'chicken-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('chicken', 'hen', 'face', 'head', 'comb', 'beak', 'farm', 'poultry')

    def build(self) -> None:
        self.add_line('left', (8, 44), (8, 29))
        self.add_arc('arch', (8, 29), (40, 29), radius_x=16, radius_y=16, sweep=True)
        self.add_line('right', (40, 29), (40, 44))
        self.add_contour('face', 'left', 'arch', 'right', closed=False)
        self.add_arc('comb-left', (24, 13), (19, 8), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('comb-top', (19, 8), (29, 8), radius_x=5, radius_y=4, sweep=True)
        self.add_arc('comb-right', (29, 8), (24, 13), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('comb', 'comb-left', 'comb-top', 'comb-right', closed=True)
        self.relate('connect', 'comb', 'face')
        self.add_dot('eye-left', (17, 28))
        self.add_dot('eye-right', (31, 28))
        self.add_polyline('beak', (19, 38), (24, 44), (29, 38))
