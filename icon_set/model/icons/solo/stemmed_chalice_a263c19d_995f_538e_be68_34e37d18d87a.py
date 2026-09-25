"""Inset rim and foot; retained the bowl, stem and triangular foot.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: wine: bowl-to-stem attachment.
"""
# Independent repair of stemmed-chalice; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a263c19d-995f-538e-be68-34e37d18d87a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/challice_a263c19d-995f-538e-be68-34e37d18d87a.svg'
AUTHOR = 'gpt-6'

class StemmedChalice(Solo48):
    icon_id = 'stemmed-chalice'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('chalice', 'goblet', 'cup', 'grail', 'wine', 'vessel', 'ceremony', 'drink', 'lucide:wine')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('rim', (8, 4), (40, 4))
        self.add_line('right', (40, 4), (40, 12))
        self.add_arc('bowl-right', (40, 12), (24, 28), radius_x=16)
        self.add_arc('bowl-left', (24, 28), (8, 12), radius_x=16)
        self.add_line('left', (8, 12), (8, 4))
        self.add_contour('bowl', 'rim', 'right', 'bowl-right', 'bowl-left', 'left', closed=True)
        self.add_line('stem', (24, 28), (24, 36))
        self.add_polyline('foot', (24, 36), (14, 44), (34, 44), closed=True)
        self.relate('connect', 'bowl', 'stem')
        self.relate('connect', 'stem', 'foot')
