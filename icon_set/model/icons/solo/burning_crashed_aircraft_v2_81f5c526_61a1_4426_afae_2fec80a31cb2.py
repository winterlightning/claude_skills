"""Burning Crashed Aircraft. Crashed aircraft, rising flame and one smoke stroke; second smoke trail removed.
Keyshape VRECT_XL: chosen for the subject's overall proportions; authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '81f5c526-61a1-4426-afae-2fec80a31cb2'
SOURCE_PATH = 'pictographic-primitives/war/plane crashed_81f5c526-61a1-4426-afae-2fec80a31cb2.svg'
AUTHOR = 'gpt-6'

class BurningCrashedAircraftVariant2(Solo48):
    icon_id = 'burning-crashed-aircraft-v2'
    variant_of = 'burning-crashed-aircraft'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('aircraft', 'crash', 'fire', 'smoke', 'flame', 'wreck')

    def build(self) -> None:
        self.add_polyline('plane', (8, 25), (20, 30), (17, 18), (27, 23), (28, 34), (40, 34), (40, 44), (25, 44), (8, 36), closed=True)
        self.add_polyline('fire', (28, 25), (26, 17), (31, 9), (30, 4), (40, 14), (40, 23), (34, 37))
        self.relate('connect', 'fire', 'plane')
        self.add_line('smoke', (12, 4), (10, 14))
