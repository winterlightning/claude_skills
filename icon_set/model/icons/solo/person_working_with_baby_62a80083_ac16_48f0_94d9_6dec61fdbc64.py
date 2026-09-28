"""A person sits behind an open laptop while cradling a small swaddled baby at the lower right. The baby's round head joins an oval wrap angled across the adult's torso.
Lucide user and baby circular head construction, with laptop construction from the earlier batch. Parent, open laptop and swaddled infant retained; face and wrap creases omitted. The baby and laptop balance a deliberately asymmetric caregiving scene.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62a80083-ac16-48f0-94d9-6dec61fdbc64'
SOURCE_PATH = 'pictographic-primitives/work/work from home user baby_62a80083-ac16-48f0-94d9-6dec61fdbc64.svg'
AUTHOR = 'gpt-6'


class PersonWorkingWithBaby(Solo48):
    icon_id = 'person-working-with-baby'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('person', 'baby', 'laptop', 'parent', 'work', 'childcare')

    def build(self) -> None:
        self.add_arc('parent-head-top', (20, 11), (30, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('parent-head-bottom', (30, 11), (20, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('parent-head', 'parent-head-top', 'parent-head-bottom', closed=True)
        self.add_polyline('laptop', (6, 24), (16, 24), (18, 30), (20, 36), (10, 36), closed=True)
        self.add_arc('parent-shoulder', (18, 30), (25, 26), radius_x=7, radius_y=4, sweep=True, large_arc=False)
        self.relate("connect", 'parent-shoulder', 'laptop')
        self.add_arc('baby-head-top', (34, 26), (42, 26), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('baby-head-bottom', (42, 26), (34, 26), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('baby-head', 'baby-head-top', 'baby-head-bottom', closed=True)
        self.add_arc('wrap-left', (38, 30), (28, 38), radius_x=10, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('wrap-bottom', (28, 38), (32, 42), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('wrap-right', (32, 42), (42, 32), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_line('wrap-top', (42, 32), (38, 30))
        self.add_contour('swaddle', 'wrap-left', 'wrap-bottom', 'wrap-right', 'wrap-top', closed=True)
        self.relate("connect", 'baby-head', 'swaddle')
