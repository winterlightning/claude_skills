"""Two standing people, one raising an arm and the other resting hands at the hips. Lucide person-standing informs the limbs. Finger shapes and doubled body outlines are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2eeb887b-b913-41a8-aaf8-0d8866ba6edb'
SOURCE_PATH = 'pictographic-primitives/users/pass through_2eeb887b-b913-41a8-aaf8-0d8866ba6edb.svg'
AUTHOR = 'gpt-6'


class TwoFiguresRaisedArm(Solo48):
    icon_id = 'two-figures-raised-arm'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('people', 'two', 'figures', 'friends', 'together', 'pass', 'gesture', 'pair')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)


    def build(self) -> None:
        # Landscape centerline extremes (6,8)-(42,40); gesture is intentionally asymmetric.
        for name,cx in (('left',17),('right',37)):
            self.circle(name+'-head',cx,13,4)
        self.add_line('left-torso',(17,27),(17,33))
        self.add_polyline('raised-arm',(17,27),(4,22),(4,8))
        self.add_line('left-low-arm',(17,27),(22,34))
        self.add_polyline('left-legs',(11,40),(17,33),(23,40))
        for part in ('raised-arm','left-low-arm','left-legs'):
            self.relate('connect','left-torso',part)
        self.relate('connect','raised-arm','left-low-arm')
        self.add_line('right-torso',(37,26),(37,33))
        self.add_polyline('right-arms',(34,34),(30,31),(37,26),(44,31),(40,34))
        self.add_polyline('right-legs',(31,40),(37,33),(44,40))
        self.relate('connect','right-torso','right-arms')
        self.relate('connect','right-torso','right-legs')
