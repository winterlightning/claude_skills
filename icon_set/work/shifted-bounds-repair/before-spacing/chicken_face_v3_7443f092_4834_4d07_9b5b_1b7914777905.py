# Bounds-only review variant; parent preserved.
"""Move every authored point down by 2 units together. Keep dimensions, arcs, shared endpoints and spacing unchanged. VRECT_L centerline box (8,4)-(40,44), ink (6,2)-(42,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'

class ChickenFaceVariant3(Solo48):
    icon_id = 'chicken-face-v3'
    variant_of = 'chicken-face'
    variant_label = 'Exact keyshape bounds'
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
        self.add_dot('eye-left', (16, 28))
        self.add_dot('eye-right', (32, 28))
        self.add_polyline('beak', (24, 35), (29, 40), (24, 44), (19, 40), (24, 35))
