"""gift heart: repaired SOLO48 composition.
Plan: Paired bow loops, central ribbon and mirrored heart lobes.
Keyshape: VRECT_L reserves height for bow, box and hanging heart.
Reduction: Double lid reduced to one top edge; heart narrowed to separate it from the box sides.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5862a2a1-e7c8-522a-812d-2db80570e593'
SOURCE_PATH = 'pictographic-primitives/rewards/gift heart_5862a2a1-e7c8-522a-812d-2db80570e593.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'gift, heart'

class Drawing(Solo48):
    icon_id = 'gift-heart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('gift', 'heart')

    def build(self):
        self.add_arc('bow-l', (16, 16), (16, 4), radius_x=6)
        self.add_line('bow-l-diagonal', (16, 4), (24, 16))
        self.add_line('bow-l-base', (24, 16), (16, 16))
        self.add_contour('bow-left', 'bow-l', 'bow-l-diagonal', 'bow-l-base', closed=True)
        self.add_arc('bow-r', (32, 4), (32, 16), radius_x=6)
        self.add_line('bow-r-base', (32, 16), (24, 16))
        self.add_line('bow-r-diagonal', (24, 16), (32, 4))
        self.add_contour('bow-right', 'bow-r', 'bow-r-base', 'bow-r-diagonal', closed=True)
        self.add_polyline('box', (18, 40), (8, 40), (8, 16), (16, 16), (24, 16), (32, 16), (40, 16), (40, 40), (30, 40))
        self.relate('connect', 'bow-left', 'bow-right', 'box')
        self.add_line('ribbon', (24, 16), (24, 30))
        self.add_bezier('heart', (24, 30), ((17, 23), (13, 34), (24, 44)), ((35, 34), (31, 23), (24, 30)))
        self.add_contour('heart-outline', 'heart', closed=True)
        self.relate('connect', 'ribbon', 'box')
        self.relate('connect', 'ribbon', 'heart-outline')
