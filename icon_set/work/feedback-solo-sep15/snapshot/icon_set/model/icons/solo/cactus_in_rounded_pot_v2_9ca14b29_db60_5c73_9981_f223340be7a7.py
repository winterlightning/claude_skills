"""Raise and lengthen both cactus branches equally. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ca14b29-db60-5c73-9981-f223340be7a7'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_9ca14b29-db60-5c73-9981-f223340be7a7.svg'
AUTHOR = 'gpt-6'

class CactusInRoundedPotVariant2(Solo48):
    icon_id = 'cactus-in-rounded-pot-v2'
    variant_of = 'cactus-in-rounded-pot'
    variant_label = 'Raise and lengthen both cactus branches equally.'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self):
        """Symbol plan: Raise and lengthen both cactus branches equally. Reference: inspected current parent; no useful exact Lucide match selected."""
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx, radius_y=rx if ry is None else ry, sweep=sweep)
        p('pot', (12, 32), (14, 44), (34, 44), (36, 32), (12, 32))
        p('stem', (20, 32), (20, 4), (28, 4), (28, 32))
        link('connect', 'pot', 'stem')
        p('left-arm', (20, 24), (8, 24), (8, 8))
        p('right-arm', (28, 24), (40, 24), (40, 8))
        link('connect', 'stem', 'left-arm')
        link('connect', 'stem', 'right-arm')
