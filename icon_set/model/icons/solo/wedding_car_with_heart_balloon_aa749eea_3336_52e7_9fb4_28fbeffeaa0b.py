# Repair: Attach the open car body at the tops of two equal circular wheels and retain the heart balloon on a curved tether.
"""A right-facing wedding car tows a heart balloon; side decal, cans and ribbon details omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa749eea-3336-52e7-9fb4-28fbeffeaa0b'
SOURCE_PATH = 'pictographic-primitives/romance/wedding car heart balloon_aa749eea-3336-52e7-9fb4-28fbeffeaa0b.svg'
AUTHOR = 'gpt-6'


class WeddingCarWithHeartBalloon(Solo48):
    icon_id = 'wedding-car-with-heart-balloon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('car', 'wedding', 'balloon', 'heart', 'vehicle', 'celebration')

    def build(self):
        from ._symmetry_curves import path, ellipse, line, poly, contacts
        # Two circular lobes define the tethered heart balloon.
        path(self,'balloon',(14,10),('A',4,4,False,(6,10)),('L',(14,20)),('L',(22,10)),('A',4,4,False,(14,10)),closed=True)
        path(self,'tether',(14,20),('A',10,10,False,(12,28)))
        path(self,'body',(12,36),('L',(12,28)),('L',(16,28)),('L',(23,24)),('L',(31,24)),('L',(34,28)),('L',(38,28)),('L',(42,28)),('L',(42,39)))
        ellipse(self,'rear-wheel',12,39,3)
        ellipse(self,'front-wheel',36,39,3)
        line(self,'sill',(15,39),(33,39))
        contacts(self)
