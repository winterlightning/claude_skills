"""Ares holding an upright spear and round shield. Keep weapon and shield hierarchy; remove belt, fingers and shield boss."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '996b003c-d419-5d2e-993e-9c6fe7388a3e'
SOURCE_PATH = 'pictographic-primitives/religion/ares_996b003c-d419-5d2e-993e-9c6fe7388a3e.svg'
AUTHOR = 'gpt-6'


class AresWithSpearAndShield(Solo48):
    icon_id = 'ares-with-spear-and-shield'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('ares', 'warrior', 'spear', 'shield', 'figure', 'mythology', 'greek')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live SQUARE centerline box (6,6)-(42,42).
        self.oval('head',21,11,5)
        self.add_polyline('spear-head',(6,14),(6,6),(8,10))
        self.add_polyline('spear',(6,14),(6,32),(6,42))
        self.relate('connect','spear','spear-head')
        self.add_arc('torso',(15,33),(23,27),radius_x=8)
        self.add_polyline('body',(15,33),(15,42),(24,42))
        self.relate('connect','torso','body')
        self.add_line('grip',(6,32),(15,33))
        self.relate('connect','grip','spear');self.relate('connect','grip','torso');self.relate('connect','grip','body')
        self.oval('shield',33,30,9)
        self.add_line('shield-arm',(23,27),(24,30))
        self.relate('connect','shield-arm','torso');self.relate('connect','shield-arm','shield')
