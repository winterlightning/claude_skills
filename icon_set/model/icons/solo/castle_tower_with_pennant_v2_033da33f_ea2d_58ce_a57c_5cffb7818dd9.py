"""Castle tower: vertical right wall and square base corner. SQUARE (2,2)-(46,46). Lucide castle informs rectilinear masonry. Original left batter and pennant retain asymmetry."""
# Variant of castle-tower-with-pennant; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '033da33f-ea2d-58ce-a57c-5cffb7818dd9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_033da33f-ea2d-58ce-a57c-5cffb7818dd9.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'castle-tower-with-pennant-v2'
    variant_of = 'castle-tower-with-pennant'
    variant_label = 'Geometric tower base'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('castle', 'tower', 'turret', 'fortress', 'battlement', 'flag', 'pennant', 'medieval')

    def build(self):
        self.add_polyline('outline', (2, 46), (6, 29), (6, 20), (14, 20), (14, 27), (22, 27), (22, 20), (30, 20), (30, 27), (38, 27), (38, 20), (46, 20), (46, 29), (46, 46), (30, 46), (18, 46), closed=True)
        self.add_polyline('flag', (22, 20), (22, 10), (22, 2), (38, 2), (34, 6), (38, 10), (22, 10))
        self.relate('connect', 'flag', 'outline')
        self.add_line('door-left', (18, 46), (18, 39))
        self.add_arc('door-top', (18, 39), (30, 39), radius_x=6)
        self.add_line('door-right', (30, 39), (30, 46))
        self.add_contour('door', 'door-left', 'door-top', 'door-right')
        self.relate('connect', 'door', 'outline')
