"""Onam floral plate: six-lobed flower within a circular rim. CIRCLE radial22 envelope; flower kept below radius12 for rim clearance."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '7d27b436-d05f-41d3-b72f-2e31759f48e2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'onam-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.CIRCLE.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('rim-a',(4,24),(44,24),radius_x=20)
        self.add_arc('rim-b',(44,24),(4,24),radius_x=20)
        self.add_contour('rim','rim-a','rim-b',closed=True)
        # Six joined lobes preserve the flower; no crowded inner petal seams.
        self.add_bezier('petals',(20,18),((20,15),(22,13),(24,13)),((26,13),(28,15),(28,18)),((30,16),(33,16),(34,18)),((35,20),(34,23),(31,24)),((34,25),(35,28),(34,30)),((33,32),(30,32),(28,30)),((28,33),(26,35),(24,35)),((22,35),(20,33),(20,30)),((18,32),(15,32),(14,30)),((13,28),(14,25),(17,24)),((14,23),(13,20),(14,18)),((15,16),(18,16),(20,18)))
        self.add_contour('flower','petals',closed=True)
