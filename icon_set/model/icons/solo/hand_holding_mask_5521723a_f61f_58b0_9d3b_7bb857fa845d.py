"""Hand Holding Mask.

Plan: Hand grips lower mask edge with a broad thumb. Lucide drama informs mask eyes; shared human references inform simplified hand. Dots replace small pointed eye holes. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5521723a-f61f-58b0-9d3b-7bb857fa845d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/cosplay_5521723a-f61f-58b0-9d3b-7bb857fa845d.svg'
AUTHOR = 'gpt-6'


class HandHoldingMask(Solo48):
    icon_id = 'hand-holding-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('hand', 'holding', 'mask')

    def build(self):
        self.add_line('mask-left',(14,30),(14,6))
        self.add_arc('mask-top',(14,6),(42,6),radius_x=14,radius_y=4,sweep=False)
        self.add_line('mask-right',(42,6),(42,22))
        self.add_arc('mask-cheek',(42,22),(31,35),radius_x=11,radius_y=13)
        self.add_contour('mask','mask-left','mask-top','mask-right','mask-cheek')
        self.add_line('wrist-left',(6,42),(6,38))
        self.add_arc('palm',(6,38),(14,30),radius_x=8)
        self.add_line('thumb-top',(14,30),(26,30))
        self.add_arc('thumb-r',(26,30),(31,35),radius_x=5)
        self.add_arc('thumb-bottom',(31,35),(26,40),radius_x=5)
        self.add_polyline('wrist-bottom',(26,40),(24,42),(6,42))
        self.add_contour('hand','wrist-left','palm','thumb-top','thumb-r','thumb-bottom','wrist-bottom-1','wrist-bottom-2',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='wrist-bottom']
        self.relate('connect','hand','mask')
        for x in [23,33]:self.add_dot(f'eye-{x}',(x,20))
