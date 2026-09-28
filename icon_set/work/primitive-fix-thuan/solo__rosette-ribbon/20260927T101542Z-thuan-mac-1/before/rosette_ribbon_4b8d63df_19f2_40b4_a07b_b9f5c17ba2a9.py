"""Scalloped award rosette with central ring and two notched tails. Lucide award informs attached tails; source scallops retained with repeated arcs.

SOLO48 VRECT_L, live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9'
SOURCE_PATH = 'pictographic-primitives/symbol/ribbon_4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9.svg'
AUTHOR = 'gpt-6'

class RosetteRibbon(Solo48):
    icon_id = 'rosette-ribbon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('rosette', 'ribbon', 'award', 'badge', 'prize', 'medal', 'winner', 'achievement')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        segments = [('top', (16, 8), (32, 8), 8, 4), ('upper-right', (32, 8), (36, 12), 4, 4), ('right', (36, 12), (36, 20), 4, 4), ('lower-right', (36, 20), (32, 24), 4, 4), ('bottom', (32, 24), (16, 24), 8, 4), ('lower-left', (16, 24), (12, 20), 4, 4), ('left', (12, 20), (12, 12), 4, 4), ('upper-left', (12, 12), (16, 8), 4, 4)]
        for name, a, b, rx, ry in segments:
            self.add_arc(name, a, b, radius_x=rx, radius_y=ry)
        self.add_contour('rosette', *[s[0] for s in segments], closed=True)
        self.add_arc('centre-top', (21, 16), (27, 16), radius_x=3)
        self.add_arc('centre-bottom', (27, 16), (21, 16), radius_x=3)
        self.add_contour('centre', 'centre-top', 'centre-bottom', closed=True)
        self.add_polyline('tails', (12, 20), (12, 44), (24, 36), (36, 44), (36, 20))
        self.relate('connect', 'rosette', 'tails')
