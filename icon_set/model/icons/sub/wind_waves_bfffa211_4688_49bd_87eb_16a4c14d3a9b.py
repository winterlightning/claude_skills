"""Wind Waves: Three separate horizontal curves form gently undulating wind lines stacked with even spacing. Each rises on the left, dips through the right half, and curls slightly upward at its ending.

Construction: Three repeated waves, each two tangent half ellipses; vertical step10 owns clearance.
Keyshape: HRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bfffa211-4688-49bd-87eb-16a4c14d3a9b'
SOURCE_PATH = 'pictographic-primitives/state/wind_bfffa211-4688-49bd-87eb-16a4c14d3a9b.svg'
AUTHOR = 'gpt-6'


class WindWaves(Sub32):
    icon_id = 'wind-waves'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ()
    keywords = ('wind', 'waves', 'separate', 'horizontal', 'curves', 'form', 'gently', 'undulating')

    def build(self):
        for i,y in enumerate((6,16,26)):
            self.add_arc(f"crest-{i}",(2,y),(16,y),radius_x=7,radius_y=2)
            self.add_arc(f"trough-{i}",(16,y),(30,y),radius_x=7,radius_y=2,sweep=False)
            self.add_contour(f"wave-{i}",f"crest-{i}",f"trough-{i}")
