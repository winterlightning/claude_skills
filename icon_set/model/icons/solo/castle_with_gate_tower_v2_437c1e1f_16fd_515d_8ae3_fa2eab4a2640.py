# Variant of castle-with-gate-tower; parent file remains unchanged.
"""A castle with a lowered arched gate and shallower battlement notch to increase clearance. SQUARE preserves tower and flag extremes; Lucide castle informs the simple arched gate."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '437c1e1f-16fd-515d-8ae3-fa2eab4a2640'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/historical building castle_437c1e1f-16fd-515d-8ae3-fa2eab4a2640.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'castle-with-gate-tower-v2'
    variant_of = 'castle-with-gate-tower'
    variant_label = 'Clearance above arched gate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('castle', 'fortress', 'gate', 'tower', 'battlement', 'spire', 'medieval', 'flag')

    def build(self):
        self.add_polyline('outline', (6, 42), (6, 24), (10, 24), (10, 28), (18, 28), (18, 24), (30, 24), (30, 16), (38, 6), (42, 16), (42, 42), (30, 42), (22, 42), (10, 42), closed=True)
        self.add_polyline('tower', (30, 16), (42, 16))
        self.add_line('tower-wall', (30, 24), (30, 42))
        self.relate('connect', 'tower', 'outline')
        self.relate('connect', 'tower-wall', 'outline')
        self.add_polyline('flag', (6, 24), (6, 12), (6, 6), (16, 6), (12, 8), (16, 12), (6, 12))
        self.relate('connect', 'flag', 'outline')
        self.add_line('door-left', (10, 42), (10, 42))
        self.add_arc('door-top', (10, 42), (22, 42), radius_x=6)
        self.add_line('door-right', (22, 42), (22, 42))
        self.add_contour('door', 'door-left', 'door-top', 'door-right')
        self.relate('connect', 'door', 'outline')
