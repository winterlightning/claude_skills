# Variant of castle-tower-with-pennant-v2; parent file remains unchanged.
"""Castle tower: vertical right wall and square base corner. SQUARE (6,6)-(42,42). Lucide castle informs rectilinear masonry. Original left batter and pennant retain asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '033da33f-ea2d-58ce-a57c-5cffb7818dd9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_033da33f-ea2d-58ce-a57c-5cffb7818dd9.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant4(Solo48):
    icon_id = 'castle-tower-with-pennant-v4'
    variant_of = 'castle-tower-with-pennant-v2'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('castle', 'tower', 'turret', 'fortress', 'battlement', 'flag', 'pennant', 'medieval')

    def build(self):
        self.add_polyline('outline', (6, 42), (6, 29), (6, 20), (14, 20), (14, 27), (22, 27), (22, 20), (30, 20), (30, 27), (38, 27), (38, 20), (42, 20), (42, 29), (42, 42), (30, 42), (18, 42), closed=True)
        self.add_polyline('flag', (22, 20), (22, 10), (22, 6), (38, 6), (34, 6), (38, 10), (22, 10))
        self.relate('connect', 'flag', 'outline')
        self.add_line('door-left', (18, 42), (18, 39))
        self.add_arc('door-top', (18, 39), (30, 39), radius_x=6)
        self.add_line('door-right', (30, 39), (30, 42))
        self.add_contour('door', 'door-left', 'door-top', 'door-right')
        self.relate('connect', 'door', 'outline')
