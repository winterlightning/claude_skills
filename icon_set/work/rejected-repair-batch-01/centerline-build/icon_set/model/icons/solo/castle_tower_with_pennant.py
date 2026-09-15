# Review revision; previous candidates preserved.
"""Castle tower: vertical right wall and square base corner. SQUARE (6,6)-(42,42). Lucide castle informs rectilinear masonry. Original left batter and pennant retain asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '033da33f-ea2d-58ce-a57c-5cffb7818dd9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_033da33f-ea2d-58ce-a57c-5cffb7818dd9.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'castle-tower-with-pennant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('castle', 'tower', 'turret', 'fortress', 'battlement', 'flag', 'pennant', 'medieval')

    def build(self):
        left, right, inner_left, inner_right = (8, 40, 16, 32)
        self.add_polyline('outline', (left, 44), (left, 20), (inner_left, 20), (inner_left, 28), (24, 28), (inner_right, 28), (inner_right, 20), (right, 20), (right, 44), (inner_right, 44), (inner_left, 44), closed=True)
        self.add_polyline('flag', (24, 28), (24, 12), (24, 4), (40, 4), (36, 8), (40, 12), (24, 12))
        self.relate('connect', 'flag', 'outline')
        self.add_arc('door', (inner_left, 44), (inner_right, 44), radius_x=8)
        self.relate('connect', 'door', 'outline')
