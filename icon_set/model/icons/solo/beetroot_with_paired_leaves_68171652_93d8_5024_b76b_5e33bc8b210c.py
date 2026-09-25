"""Beetroot With Two Leaves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68171652-93d8-5024-b76b-5e33bc8b210c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/beet_68171652-93d8-5024-b76b-5e33bc8b210c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'beetroot-with-paired-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('beetroot', 'beet', 'root', 'leaf', 'vegetable', 'produce', 'food')

    def build(self):
        # Plan: Pointed bulb supports a branching stem and two broad mirrored leaf outlines. Lucide sprout for paired leaves. Bounds (8,4)-(40,44).
        a=24
        self.add_bezier('bulb',(a,26),((32,26),(40,26),(40,32)),((40,38),(29,39),(a,44)),((19,39),(8,38),(8,32)),((8,26),(16,26),(a,26)))
        self.add_contour('root','bulb',closed=True)
        self.add_polyline('stem',(20,16),(a,20),(a,26))
        self.add_line('branch-right',(a,20),(28,16));self.relate('connect','branch-right','stem');self.relate('connect','stem','root')
        for side in (-1,1):
            tip=(a+side*16,4);end=(a+side*4,16)
            self.add_bezier(f'leaf-{side}',tip,((a+side*7,4),(a+side*4,7),end),((a+side*13,16),(a+side*16,13),tip))
            self.add_contour(f'leaf-outline-{side}',f'leaf-{side}',closed=True)
        self.relate('connect','leaf-outline--1','stem');self.relate('connect','leaf-outline-1','branch-right')
