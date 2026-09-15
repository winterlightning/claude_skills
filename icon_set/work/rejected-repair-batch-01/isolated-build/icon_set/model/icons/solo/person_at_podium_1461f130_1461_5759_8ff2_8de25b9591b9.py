"""A round-headed speaker with arched shoulders behind a lectern. Lucide user-round informs the shoulders. Small hand details are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1461f130-1461-5759-8ff2-8de25b9591b9'
SOURCE_PATH = 'pictographic-primitives/users/neutral podium_1461f130-1461-5759-8ff2-8de25b9591b9.svg'
AUTHOR = 'gpt-6'


class PersonAtPodium(Solo48):
    icon_id = 'person-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('person', 'podium', 'lectern', 'speaker', 'presentation', 'speech', 'talk', 'conference')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)


    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42).
        self.circle('head',24,11,5)
        self.add_arc('shoulder-left',(12,33),(20,25),radius_x=8)
        self.add_line('shoulder-top',(20,25),(28,25))
        self.add_arc('shoulder-right',(28,25),(36,33),radius_x=8)
        self.add_contour('shoulders','shoulder-left','shoulder-top','shoulder-right')
        self.add_polyline('lectern',(6,33),(12,33),(36,33),(42,33))
        self.add_line('leg-left',(12,33),(10,42))
        self.add_line('leg-right',(36,33),(38,42))
        self.relate('connect','lectern','shoulders')
        for name in ('leg-left','leg-right'):
            self.relate('connect','lectern',name)
            self.relate('connect','shoulders',name)
