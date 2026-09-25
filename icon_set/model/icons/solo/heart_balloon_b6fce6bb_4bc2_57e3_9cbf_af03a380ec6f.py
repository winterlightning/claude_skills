"""A heart balloon has a knot and a gently bending string; the knot is an open chevron.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f'
SOURCE_PATH = 'pictographic-primitives/romance/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg'
AUTHOR = 'gpt-6'


class HeartBalloon(Solo48):
    icon_id = 'heart-balloon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
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
        self.relate('connect','balloon','knot')
        self.add_arc('string-a',(24,30),(22,37),radius_x=10,sweep=False)
        self.add_arc('string-b',(22,37),(24,44),radius_x=10)
        self.add_contour('string','string-a','string-b')
        self.relate('connect','balloon','string')
        self.relate('connect','knot','string')
