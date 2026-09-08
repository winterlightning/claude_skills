"""Upright-horn rhinoceros profile with blunt low jaw and rear ear. Centerline (8,2)-(40,46). Asymmetry follows profile."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f24f610-9641-44f3-9d96-40bea7d2f1ae'
SOURCE_PATH = 'pictographic-primitives/animals/rhinoceros head_3f24f610-9641-44f3-9d96-40bea7d2f1ae.svg'
AUTHOR = 'gpt-6'


class RhinoHeadProfile(Solo48):
    icon_id = 'rhino-head-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('rhino', 'rhinoceros', 'head', 'horn', 'ears', 'profile', 'animal', 'wildlife')

    def build(self) -> None:
        self.add_arc('top-1', (40, 8), (27, 12), radius_x=18, radius_y=12, sweep=True)
        self.add_line('top-2', (27, 12), (27, 2))
        self.add_line('top-3', (27, 2), (20, 9))
        self.add_arc('top-4', (20, 9), (20, 19), radius_x=10, radius_y=10, sweep=False)
        self.add_line('top-5', (20, 19), (15, 23))
        self.add_arc('top-6', (15, 23), (8, 2), radius_x=40, radius_y=40, sweep=True)
        self.add_line('top-7', (8, 2), (8, 17))
        self.add_arc('top-8', (8, 17), (12, 31), radius_x=4, radius_y=14, sweep=False)
        self.add_contour('top', 'top-1', 'top-2', 'top-3', 'top-4', 'top-5', 'top-6', 'top-7', 'top-8', closed=False)
        self.add_arc('jaw-1', (12, 31), (8, 38), radius_x=9, radius_y=9, sweep=False)
        self.add_arc('jaw-2', (8, 38), (16, 46), radius_x=8, radius_y=8, sweep=False)
        self.add_line('jaw-3', (16, 46), (29, 46))
        self.add_arc('jaw-4', (29, 46), (40, 35), radius_x=11, radius_y=11, sweep=False)
        self.add_contour('jaw', 'jaw-1', 'jaw-2', 'jaw-3', 'jaw-4', closed=False)
        self.relate("connect", 'top', 'jaw')
        self.add_dot('eye', (29, 28))
