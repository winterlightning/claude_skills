"""A light bulb with a round glass top narrowing into a short stepped base.

Plan: Mirrored bulb about x=24; semicircular dome flows into paired shoulder curves; detached base.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: lightbulb: dome, smooth shoulders, detached base.
Simplification: Stepped socket reduced to one detached base stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0fc333fe-a7cf-4836-b02f-2467e5c78a5b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-keep-bulb-logo/20260927T055654Z-thuan-mac-1/reference/google keep logo 1_0fc333fe-a7cf-4836-b02f-2467e5c78a5b.svg'
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
        self.add_line('base',(18,44),(30,44))
        self.add_line('base-left',(18,35),(18,44))
        self.add_line('base-right',(30,35),(30,44))
        for part in ('base-left','base-right'):
            self.relate('connect',part,'glass')
            self.relate('connect',part,'base')
