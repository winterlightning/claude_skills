"""Bok Choy Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0872b18e-4421-5494-9d4c-57bf85fc531e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/bok shoy_0872b18e-4421-5494-9d4c-57bf85fc531e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bok-choy-bunch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('bok choy', 'leaf', 'vegetable', 'greens', 'stalk', 'produce', 'food')

    def build(self):
        # Plan: Three leafy lobes with a single shared midrib. Lucide leafy-green; veins reduced for clearance. Upright envelope (8,4)-(40,44).
        self.add_bezier('leaf',(14,14),((14,8),(18,4),(24,4)),((30,4),(34,8),(34,14)),((37,10),(40,13),(40,20)),((40,28),(34,30),(34,37)),((34,42),(28,44),(24,44)),((20,44),(14,42),(14,37)),((14,30),(8,28),(8,20)),((8,13),(11,10),(14,14)))
        self.add_contour('leaves','leaf',closed=True)
        self.add_line('midrib',(24,14),(24,44));self.relate('connect','midrib','leaves')
