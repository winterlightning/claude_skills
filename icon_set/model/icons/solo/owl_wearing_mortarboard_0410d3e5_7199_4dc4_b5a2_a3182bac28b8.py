"""An owl wears a diamond mortarboard. The supplied owl establishes eyes and beak; no useful Lucide owl match exists. Lucide graduation-cap informs the cap. Wings and cap band are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0410d3e5-7199-4dc4-b5a2-a3182bac28b8'
SOURCE_PATH = 'pictographic-primitives/school-learning/study owl_0410d3e5-7199-4dc4-b5a2-a3182bac28b8.svg'
AUTHOR = 'gpt-6'


class OwlWearingMortarboard(Solo48):
    icon_id = 'owl-wearing-mortarboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "education/school"
    aliases = ()
    keywords = ('owl', 'mortarboard', 'graduation', 'education', 'bird', 'study')

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

        self.add_polyline('cap',(6,12),(24,6),(42,12),(24,18),closed=True)
        self.add_line('tassel',(6,12),(6,20))
        self.relate('connect','cap','tassel')
        for side,x in (('left',15),('right',33)):
            self.circle('eye-'+side,x,29,4)
        self.add_arc('body-left',(11,29),(24,42),radius_x=13,sweep=False)
        self.add_arc('body-right',(24,42),(37,29),radius_x=13,sweep=False)
        self.add_contour('body','body-left','body-right')
        self.relate('connect','eye-left','body')
        self.relate('connect','eye-right','body')
        self.add_polyline('beak',(19,29),(24,33),(29,29))
        self.relate('connect','beak','eye-left')
        self.relate('connect','beak','eye-right')
