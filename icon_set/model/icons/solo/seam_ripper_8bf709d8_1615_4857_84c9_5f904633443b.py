"""Seam Ripper.

Plan: Diagonal rounded grip and long shaft ending in an open hook. One loose thread curls right. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8bf709d8-1615-4857-84c9-5f904633443b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/sew tool_8bf709d8-1615-4857-84c9-5f904633443b.svg'
AUTHOR = 'gpt-6'

class SeamRipper(Solo48):
    icon_id = 'seam-ripper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('seam', 'ripper')

    def build(self):
        self.add_arc('grip-top',(32,8),(40,14),radius_x=5)
        self.add_polyline('grip-right',(40,14),(30,26),(26,22),(22,18),(32,8))
        self.add_contour('grip','grip-top','grip-right-1','grip-right-2','grip-right-3','grip-right-4',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='grip-right']
        self.add_line('shaft',(26,22),(6,38))
        self.add_arc('hook',(6,38),(10,42),radius_x=4,sweep=False)
        self.add_line('hook-tip',(10,42),(14,42))
        self.add_contour('tool','shaft','hook','hook-tip');self.relate('connect','tool','grip')
        self.add_arc('thread',(26,38),(42,38),radius_x=8,radius_y=4,sweep=False)
