# Refinement: Shorten both figures lowered forearms to separate the hands from the legs and from each other.
# Repair: Shorten the left figure free arm so it no longer crowds either leg.
"""Two standing people, one raising an arm and the other resting hands at the hips. Lucide person-standing informs the limbs. Finger shapes and doubled body outlines are omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2eeb887b-b913-41a8-aaf8-0d8866ba6edb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-figures-raised-arm/20260927T101610Z-thuan-mac-1/reference/pass through_2eeb887b-b913-41a8-aaf8-0d8866ba6edb.svg'
AUTHOR = "gpt-6"

class TwoFiguresRaisedArm(Solo48):
    icon_id = 'two-figures-raised-arm'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('people', 'two', 'figures', 'friends', 'together', 'pass', 'gesture', 'pair')

    def circle(self, name, cx, cy, r):
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)]
        ids = []
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            eid = name + '-' + str(i)
            self.add_arc(eid, a, b, radius_x=r)
            ids.append(eid)
        self.add_contour(name, *ids, closed=True)

    def build(self) -> None:
        """Two distinct figures; the left raises its right arm toward the source's open upper corner."""
        for n,x in (('left',11),('right',38)):
            self.circle(n+'-head',x,12,4)
            self.add_line(n+'-torso',(x,25),(x,34))
        self.add_polyline('left-legs',(5,40),(11,34),(17,40))
        self.add_line('left-lowered-arm',(11,25),(4,28))
        self.add_polyline('left-raised-arm',(11,25),(21,25),(26,8))
        self.add_polyline('right-legs',(32,40),(38,34),(44,40))
        self.add_line('right-left-arm',(38,25),(31,28))
        self.add_line('right-right-arm',(38,25),(44,28))
        for n in ('left','right'):
            self.relate('connect',n+'-torso',n+'-legs')
            self.mark_human_figure(n,head=n+'-head',torso=n+'-torso',torso_junction='start')
        for part in ('left-lowered-arm','left-raised-arm'):
            self.relate('connect','left-torso',part)
        for part in ('right-left-arm','right-right-arm'):
            self.relate('connect','right-torso',part)
