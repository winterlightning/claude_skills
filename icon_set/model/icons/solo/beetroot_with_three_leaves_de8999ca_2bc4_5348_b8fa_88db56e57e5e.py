"""Beet Root Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de8999ca-2bc4-5348-b8fa-88db56e57e5e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/garlic root_de8999ca-2bc4-5348-b8fa-88db56e57e5e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'beetroot-with-three-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('beetroot', 'root', 'vegetable', 'leaf', 'produce', 'food', 'garden')

    def build(self):
        # Plan: Broad pointed beet bulb beneath three radiating leaf strokes. Rootlets reduced to one tip. Lucide carrot informs simple foliage; mirrored side stalks. Bounds (8,4)-(40,44).
        a=24
        self.add_bezier('bulb',(a,25),((13,19),(8,24),(8,30)),((8,36),(17,41),(a,44)),((31,41),(40,36),(40,30)),((40,24),(35,19),(a,25)))
        self.add_contour('root','bulb',closed=True)
        self.add_line('middle-leaf',(a,4),(a,25));self.relate('connect','middle-leaf','root')
        for side in (-1,1):
            self.add_bezier(f'leaf-{side}',(a+side*16,9),((a+side*15,17),(a+side*5,19),(a,25)))
            self.relate('connect',f'leaf-{side}','root');self.relate('connect',f'leaf-{side}','middle-leaf')
        self.relate('connect','leaf--1','leaf-1')
