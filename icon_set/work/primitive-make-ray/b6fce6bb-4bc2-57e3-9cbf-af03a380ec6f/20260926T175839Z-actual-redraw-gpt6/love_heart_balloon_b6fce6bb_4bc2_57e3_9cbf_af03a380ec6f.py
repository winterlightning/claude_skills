"""A heart balloon has a narrow neck and a gently bending string; the bulky knot is omitted for clarity.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-balloon/20260926T172218Z-thuan-mac-1/reference/love heart balloon_b6fce6bb-4bc2-57e3-9cbf-af03a380ec6f.svg'
AUTHOR = 'gpt-6'


class HeartBalloon(Solo48):
    icon_id = 'heart-balloon'
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
        # One narrow neck and one curved string avoid the inked-over crossing.
        self.add_line('neck',(24,30),(24,34))
        self.relate('connect','balloon','neck')
        self.add_arc('string',(24,34),(24,44),radius_x=8,sweep=False)
        self.relate('connect','neck','string')
