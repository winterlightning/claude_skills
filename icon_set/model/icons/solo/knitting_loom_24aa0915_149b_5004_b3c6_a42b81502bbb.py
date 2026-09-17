"""Knitting Loom.

Plan: Three rounded loom pegs rising from a rounded base, with broad yarn dips between. Shared pitch 16 and radius 4. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24aa0915-149b-5004-b3c6-a42b81502bbb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/knitting loom_24aa0915-149b-5004-b3c6-a42b81502bbb.svg'
AUTHOR = 'gpt-6'

class KnittingLoom(Solo48):
    icon_id = 'knitting-loom'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('knitting', 'loom')

    def build(self):
        self.add_polyline('base',(4,24),(4,36))
        self.add_arc('base-bl',(4,36),(8,40),radius_x=4,sweep=False)
        self.add_line('bottom',(8,40),(40,40))
        self.add_arc('base-br',(40,40),(44,36),radius_x=4,sweep=False)
        self.add_line('side-r',(44,36),(44,24))
        self.add_contour('base-outline','base-1','base-bl','bottom','base-br','side-r')
        self.contours=[c for c in self.contours if c.contour_id!='base']
        for i in range(3):
         x=8+16*i
         self.add_line(f'peg-l-{i}',(x-4,24),(x-4,12))
         self.add_arc(f'peg-top-{i}',(x-4,12),(x+4,12),radius_x=4)
         self.add_line(f'peg-r-{i}',(x+4,12),(x+4,24))
         self.add_contour(f'peg-{i}',f'peg-l-{i}',f'peg-top-{i}',f'peg-r-{i}')
        for i in range(2):
         x=12+16*i
         self.add_arc(f'yarn-{i}',(x,24),(x+8,24),radius_x=4,sweep=False)
         self.relate('connect',f'yarn-{i}',f'peg-{i}');self.relate('connect',f'yarn-{i}',f'peg-{i+1}')
        self.relate('connect','base-outline','peg-0');self.relate('connect','base-outline','peg-2')
