"""A light bulb with a round glass top narrowing into a short stepped base.

Plan: Mirrored bulb about x=24; semicircular dome flows into paired shoulder curves; detached base.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: lightbulb: dome, smooth shoulders, detached base.
Simplification: Stepped socket reduced to one detached base stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fc333fe-a7cf-4836-b02f-2467e5c78a5b'
SOURCE_PATH = 'pictographic-primitives/logos/google keep logo 1_0fc333fe-a7cf-4836-b02f-2467e5c78a5b.svg'
AUTHOR = 'gpt-6'


class GoogleKeepBulbLogo(Solo48):
    icon_id = 'google-keep-bulb-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-keep', 'google', 'lightbulb', 'notes', 'idea', 'logo', 'brand')

    def build(self):
        self.add_arc('dome',(8,20),(40,20),radius_x=16)
        self.add_bezier('right',(40,20),((40,28),(30,30),(30,35)))
        self.add_line('neck',(30,35),(18,35))
        self.add_bezier('left',(18,35),((18,30),(8,28),(8,20)))
        self.add_contour('glass','dome','right','neck','left',closed=True)
        self.add_line('base',(19,44),(29,44))
