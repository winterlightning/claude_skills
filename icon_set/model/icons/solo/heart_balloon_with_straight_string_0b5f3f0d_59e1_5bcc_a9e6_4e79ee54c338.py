"""A heart balloon has a straight string and open knot; the tiny enclosed knot is simplified.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b5f3f0d-59e1-5bcc-a9e6-4e79ee54c338'
SOURCE_PATH = 'pictographic-primitives/romance/romance pride lgbt heart balloon_0b5f3f0d-59e1-5bcc-a9e6-4e79ee54c338.svg'
AUTHOR = 'gpt-6'


class HeartBalloonWithStraightString(Solo48):
    icon_id = 'heart-balloon-with-straight-string'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('heart', 'balloon', 'string', 'party', 'romance', 'celebration')

    def build(self) -> None:
        self.add_arc('lobe-l',(24,12),(8,12),radius_x=8,sweep=False)
        self.add_arc('shoulder-l',(8,12),(12,20),radius_x=10,sweep=False)
        self.add_line('side-l',(12,20),(24,30))
        self.add_line('side-r',(24,30),(36,20))
        self.add_arc('shoulder-r',(36,20),(40,12),radius_x=10,sweep=False)
        self.add_arc('lobe-r',(40,12),(24,12),radius_x=8,sweep=False)
        self.add_contour('balloon','lobe-l','shoulder-l','side-l','side-r','shoulder-r','lobe-r',closed=True)
        self.add_polyline('knot',(20,34),(24,30),(28,34))
        self.add_line('string',(24,30),(24,44))
        self.relate('connect','balloon','knot')
        self.relate('connect','balloon','string')
        self.relate('connect','knot','string')
