"""A rounded two-door cabinet stands on short feet. Lucide panels-top-left informs matching corner radii and shared seams. Short label slots and vertical handles remain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afacc7dd-413c-5766-b512-db08c19f51d3'
SOURCE_PATH = 'pictographic-primitives/school-learning/school locker_afacc7dd-413c-5766-b512-db08c19f51d3.svg'
AUTHOR = 'gpt-6'


class TwoDoorSchoolLocker(Solo48):
    icon_id = 'two-door-school-locker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('locker', 'cabinet', 'school', 'storage', 'door', 'furniture')

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

        self.run('top',(10,6),(24,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,32))
        self.add_arc('br',(42,32),(38,36),radius_x=4)
        self.run('bottom',(38,36),(34,36),(24,36),(14,36),(10,36))
        self.add_arc('bl',(10,36),(6,32),radius_x=4)
        self.add_line('left',(6,32),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('frame','top-1','top-2','tr','right','br','bottom-1','bottom-2','bottom-3','bottom-4','bl','left','tl',closed=True)
        self.add_line('seam',(24,6),(24,36))
        self.relate('connect','frame','seam')
        for side,x,d in (('left',15,1),('right',33,-1)):
            self.add_line('label-'+side,(x,15),(x+d,15))
            self.add_line('handle-'+side,(x,24),(x,27))
        for side,x in (('left',14),('right',34)):
            self.add_line('foot-'+side,(x,36),(x,42))
            self.relate('connect','frame','foot-'+side)
