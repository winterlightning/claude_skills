"""Downward-facing rhino head, open neck and sweeping jaw. Source sets tilt and single horn. Centerline (2,5)-(46,43)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49084bcd-be73-4a9a-8269-a4edda527965'
SOURCE_PATH = 'pictographic-primitives/animals/rhino_49084bcd-be73-4a9a-8269-a4edda527965.svg'
AUTHOR = 'gpt-6'


class RhinoHead(Solo48):
    icon_id = 'rhino-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('rhino', 'rhinoceros', 'head', 'horn', 'ear', 'profile', 'animal', 'wildlife')

    def build(self) -> None:
        self.add_arc('upper-1', (2, 5), (14, 9), radius_x=20, radius_y=12, sweep=True)
        self.add_line('upper-2', (14, 9), (18, 5))
        self.add_arc('upper-3', (18, 5), (20, 20), radius_x=8, radius_y=12, sweep=True)
        self.add_line('upper-4', (20, 20), (29, 25))
        self.add_line('upper-5', (29, 25), (36, 14))
        self.add_arc('upper-6', (36, 14), (38, 30), radius_x=12, radius_y=14, sweep=True)
        self.add_line('upper-7', (38, 30), (40, 31))
        self.add_arc('upper-8', (40, 31), (46, 37), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('upper', 'upper-1', 'upper-2', 'upper-3', 'upper-4', 'upper-5', 'upper-6', 'upper-7', 'upper-8', closed=False)
        self.add_arc('jaw-1', (46, 37), (40, 43), radius_x=6, radius_y=6, sweep=True)
        self.add_line('jaw-2', (40, 43), (14, 34))
        self.add_arc('jaw-3', (14, 34), (5, 26), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('jaw', 'jaw-1', 'jaw-2', 'jaw-3', closed=False)
        self.relate("connect", 'upper', 'jaw')
        self.add_dot('eye', (24, 30))
