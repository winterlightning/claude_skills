# Variant of user; parent file remains unchanged.
"""A round head above domed shoulders and a flat base. Lucide user-round informs the circular head and coherent shoulder arch. No defining feature omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14b63c9c-a856-48d1-83f1-c289ae406875'
SOURCE_PATH = 'pictographic-primitives/users/neutral_14b63c9c-a856-48d1-83f1-c289ae406875.svg'
AUTHOR = 'gpt-6'

class UserVariant2(Solo48):
    icon_id = 'user-v2'
    variant_of = 'user'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/users'
    aliases = ()
    keywords = ('user', 'person', 'account', 'profile', 'avatar', 'member', 'human', 'neutral')

    def circle(self, name, cx, cy, r):
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        ids = []
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(i)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

    def build(self) -> None:
        self.circle('head', 24, 12, 8)
        self.add_arc('shoulders', (8, 42), (40, 42), radius_x=16, radius_y=15)
        self.add_line('base', (40, 42), (8, 42))
        self.add_contour('bust', 'shoulders', 'base', closed=True)
