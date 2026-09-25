"""ribbon 2: standalone batch 17 repair.
Retained the circular medal and both forked ribbon tails. Used a smaller medal and lower attachment points to enlarge the tail openings; mirrored all paired geometry.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '0c3535ed-6772-4bdc-aea7-fb01cc99793c'
SOURCE_PATH = 'pictographic-primitives/other/ribbon 2_0c3535ed-6772-4bdc-aea7-fb01cc99793c.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'award'

class Drawing(Solo48):
    icon_id = 'ribbon-2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('ribbon', '2')

    def build(self):
        # Circle nodes from a 5-12-13 triangle leave more height for the tails.
        pts=[(11,19),(24,6),(37,19),(36,24),(24,32),(12,24)]
        for i in range(len(pts)):
            self.add_arc(f'medal-{i}',pts[i],pts[(i+1)%len(pts)],radius_x=13)
        self.add_contour('medal',*(f'medal-{i}' for i in range(len(pts))),closed=True)
        for side in [0,1]:
            def p(x,y):return (48-x if side else x,y)
            self.add_polyline(f'tail-{side}',p(12,24),p(6,38),p(14,36),p(18,42),p(24,32))
            self.relate('connect','medal',f'tail-{side}')
        self.relate('connect','tail-0','tail-1')

