"""A mortarboard has a diamond top, curved band, and left tassel. Lucide graduation-cap informs the joined top and elliptical band; the small pendant is reduced to the cord end."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb3f11d5-9b95-5744-9a07-daba9c233e24'
SOURCE_PATH = 'pictographic-primitives/school-learning/graduation hat_bb3f11d5-9b95-5744-9a07-daba9c233e24.svg'
AUTHOR = 'gpt-6'


class MortarboardCap(Solo48):
    icon_id = 'mortarboard-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('graduation', 'cap', 'mortarboard', 'school', 'academic', 'tassel')

    def run(self, name, *points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(name+"-"+str(j),a,b)

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self) -> None:
        # Current centerline bounds: SQUARE 6,6-42,42; HRECT 4,8-44,40; VRECT 8,4-40,44.

        self.add_polyline('top',(4,18),(24,8),(44,18),(34,23),(24,28),(14,23),closed=True)
        self.add_line('band-left',(14,23),(14,32))
        self.add_arc('band-bottom',(14,32),(34,32),radius_x=10,radius_y=6,sweep=False)
        self.add_line('band-right',(34,32),(34,23))
        self.add_contour('band','band-left','band-bottom','band-right')
        self.add_line('tassel',(4,18),(4,40))
        self.relate('connect','top','band')
        self.relate('connect','top','tassel')
