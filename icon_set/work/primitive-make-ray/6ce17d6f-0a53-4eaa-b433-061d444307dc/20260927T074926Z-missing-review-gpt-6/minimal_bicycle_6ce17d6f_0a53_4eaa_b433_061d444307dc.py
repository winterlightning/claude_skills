"""Revision of minimal-bicycle. Redrew the two wheels and front fork with a vertical final section so the fork meets the tire without a narrow wedge.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""A minimal bicycle with plain wheels, an open frame and a handlebar turned back toward the rider. HRECT_L ink (6,6)-(42,42). Lucide bike informed equal circular wheels; all three identical source references are retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6ce17d6f-0a53-4eaa-b433-061d444307dc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__minimal-bicycle/20260927T074149Z-thuan-mac-1/reference/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'
SOURCE_REFERENCES = (('6ce17d6f-0a53-4eaa-b433-061d444307dc', 'pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg'), ('809ac450-efd8-4c1a-94b3-ed96c86e92df', 'pictographic-primitives/transportation/bicycle_809ac450-efd8-4c1a-94b3-ed96c86e92df.svg'), ('c94a3698-f47d-459c-afbc-fc5e64f7a783', 'pictographic-primitives/transportation/bicycle_c94a3698-f47d-459c-afbc-fc5e64f7a783.svg'))
AUTHOR = 'gpt-6'

class MinimalBicycle(Solo48):
    icon_id = 'minimal-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('bicycle', 'bike', 'cycling', 'simple', 'pedal', 'transport', 'two wheels', 'ride')

    def build(self):
        for side,x in [('rear',10),('front',38)]:
            self.add_arc(side+'-right',(x,28),(x,40),radius_x=6)
            self.add_arc(side+'-left',(x,40),(x,28),radius_x=6)
            self.add_contour(side+'-wheel',side+'-right',side+'-left',closed=True)
        self.add_polyline('frame',(10,28),(19,16),(26,28),(10,28))
        self.add_polyline('seat',(16,8),(22,8),(19,16))
        self.add_polyline('fork',(26,28),(31,16),(38,16),(38,28))
        self.add_polyline('handlebar',(31,16),(29,8),(25,8))
        for a,b in [('frame','rear-wheel'),('seat','frame'),('fork','frame'),('fork','front-wheel'),('handlebar','fork')]:
            self.relate('connect',a,b)
