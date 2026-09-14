# Variant of chateau-frontenac; parent file remains unchanged.
"""Château with separated roof peaks and an arched entrance; front turret and secondary eave removed to open crowded roof junctions. HRECT_L visible bounds (2,6)-(46,42). No useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ba45a21-4375-538a-afb6-e6d71151d5e5'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/chateau frontenac canada_8ba45a21-4375-538a-afb6-e6d71151d5e5.svg'
AUTHOR = 'gpt-6'

class LandmarkVariant2(Solo48):
    icon_id = 'chateau-frontenac-v2'
    variant_of = 'chateau-frontenac'
    variant_label = 'Roomier spacing — review 02'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('chateau', 'frontenac', 'quebec', 'canada', 'hotel', 'castle', 'landmark', 'architecture', 'turret')

    def build(self):
        self.add_polyline('outline',(4,40),(4,26),(10,16),(16,26),(20,16),(24,8),(32,8),(36,16),(36,26),(38,26),(44,32),(44,40),(30,40),(20,40),closed=True)
        self.add_line('main-eave',(20,16),(36,16))
        self.relate('connect','main-eave','outline')
        self.add_line('door-left',(20,40),(20,35))
        self.add_arc('door-top',(20,35),(30,35),radius_x=5)
        self.add_line('door-right',(30,35),(30,40))
        self.add_contour('door','door-left','door-top','door-right')
        self.relate('connect','door','outline')
