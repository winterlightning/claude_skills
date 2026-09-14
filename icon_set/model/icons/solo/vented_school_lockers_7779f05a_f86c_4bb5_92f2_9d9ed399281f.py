"""Two vented locker doors share a frame. Lucide panels-top-left informs the split frame. Vent pairs are reduced to one top and one bottom slot per door; central handle dots remain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7779f05a-f86c-4bb5-92f2-9d9ed399281f'
SOURCE_PATH = 'pictographic-primitives/school-learning/school locker closed_7779f05a-f86c-4bb5-92f2-9d9ed399281f.svg'
AUTHOR = 'gpt-6'


class VentedSchoolLockers(Solo48):
    icon_id = 'vented-school-lockers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('locker', 'school', 'storage', 'door', 'vent', 'cabinet')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+'-'+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Live centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40.

        self.add_polyline('frame',(6,6),(24,6),(42,6),(42,42),(24,42),(6,42),closed=True)
        self.add_line('seam',(24,6),(24,42))
        self.relate('connect','frame','seam')
        for side,x in (('left',15),('right',33)):
            for level,y in (('top',14),('bottom',34)):
                self.add_line(side+'-'+level+'-vent',(x-1,y),(x+1,y))
            self.add_dot(side+'-handle',(x,24))
