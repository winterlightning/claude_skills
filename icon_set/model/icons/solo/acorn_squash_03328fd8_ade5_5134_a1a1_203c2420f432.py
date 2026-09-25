"""Acorn Squash Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03328fd8-ade5-5134-a1a1-203c2420f432'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/acornsquash_03328fd8-ade5-5134-a1a1-203c2420f432.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'acorn-squash'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('squash', 'acorn squash', 'vegetable', 'gourd', 'harvest', 'food', 'stem')

    def build(self):
        # Plan: Broad squash owns two mirrored ribs and a curved stem. Shared vertical axis and lower junction. Three lobes retained. Lucide apple for coherent bulging outline. Bounds (8,4)-(40,44).
        a=24
        self.add_bezier('outer',(a,14),((13,9),(8,15),(8,26)),((8,37),(15,44),(a,44)),((33,44),(40,37),(40,26)),((40,15),(35,9),(a,14)))
        self.add_contour('body','outer',closed=True)
        for side in (-1,1):
            self.add_bezier(f'rib-{side}',(a,14),((a+side*9,16),(a+side*10,34),(a,44)))
            self.relate('connect',f'rib-{side}','body')
        self.add_bezier('stem',(a,14),((22,10),(24,6),(28,4)))
        self.relate('connect','stem','body')
