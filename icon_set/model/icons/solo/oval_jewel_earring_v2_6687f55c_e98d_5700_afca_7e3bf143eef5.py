"""Enlarged the oval jewel and inset the open hook; retained the hook, post and jewel.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6687f55c-e98d-5700-afca-7e3bf143eef5'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/earring jewel_6687f55c-e98d-5700-afca-7e3bf143eef5.svg'
AUTHOR = 'gpt-6'

class OvalJewelEarringVariant2(Solo48):
    icon_id = 'oval-jewel-earring-v2'
    variant_of = 'oval-jewel-earring'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('earring', 'jewel', 'oval', 'hook', 'jewellery', 'jewelry', 'drop', 'accessory', 'gem')

    def build(self) -> None:
        # VRECT_L (8,4)-(40,44). Shared axis, open hook above a broad oval jewel.
        x=24
        self.add_arc('hook-top',(14,10),(34,10),radius_x=10,radius_y=6)
        self.add_arc('hook-return',(x,16),(14,10),radius_x=10,radius_y=6)
        self.add_contour('hook','hook-return','hook-top')
        self.add_line('post',(x,16),(x,20))
        self.add_arc('jewel-right',(x,20),(x,44),radius_x=16,radius_y=12)
        self.add_arc('jewel-left',(x,44),(x,20),radius_x=16,radius_y=12)
        self.add_contour('jewel','jewel-right','jewel-left',closed=True)
        self.relate('connect','hook','post')
        self.relate('connect','post','jewel')
