"""A woman with two outward hair flicks above a flared dress. Lucide user-round informs the head; the reference supplies the hair flicks and dress. Tiny facial details are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '945e9ef0-3098-5263-999a-e473cba0d938'
SOURCE_PATH = 'pictographic-primitives/users/primitive symbols woman_945e9ef0-3098-5263-999a-e473cba0d938.svg'
AUTHOR = 'gpt-6'

class WomanFigure(Solo48):
    icon_id = 'woman-figure'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/users'
    aliases = ()
    keywords = ('woman', 'female', 'figure', 'person', 'dress', 'gender', 'girl', 'user')

    def circle(self, name, cx, cy, r):
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        ids = []
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(i)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.circle('head', 24, 12, 8)
        for side, direction in (('left', -1), ('right', 1)):
            x = 24 + direction * 8
            tip = 24 + direction * 12
            self.add_line('hair-' + side + '-stem', (x, 12), (x, 16))
            self.add_arc('hair-' + side + '-flick', (x, 16), (tip, 20), radius_x=4, sweep=direction < 0)
            self.add_contour('hair-' + side, 'hair-' + side + '-stem', 'hair-' + side + '-flick')
            self.relate('connect', 'head', 'hair-' + side)
        self.add_arc('dress-neck', (20, 30), (28, 30), radius_x=4, radius_y=2)
        self.add_line('dress-right', (28, 30), (40, 44))
        self.add_line('dress-hem', (40, 44), (8, 44))
        self.add_line('dress-left', (8, 44), (20, 30))
        self.add_contour('dress', 'dress-neck', 'dress-right', 'dress-hem', 'dress-left', closed=True)
