"""Three women form a triangle, with fringes and lower shoulder silhouettes. Lucide users-round informs the grouping; tiny eyes, ears, and the lower hair curls are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7507033-a4fb-4857-8a9a-208685a6411c'
SOURCE_PATH = 'pictographic-primitives/users/user multiple half female group_e7507033-a4fb-4857-8a9a-208685a6411c.svg'
AUTHOR = 'gpt-6'


class ThreeWomenPyramid(Solo48):
    icon_id = 'three-women-pyramid'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('women', 'group', 'three', 'team', 'female', 'users', 'people', 'community')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)


    def build(self) -> None:
        # Landscape centerline extremes (6,8)-(42,40); lower pair mirrors x=24.
        self.circle('top-head',24,14,6)
        self.add_line('top-fringe',(18,14),(30,14))
        self.relate('connect','top-head','top-fringe')
        for side,direction in (('left',-1),('right',1)):
            self.add_line('top-hair-'+side,(24+direction*6,14),(24+direction*7,18))
            self.relate('connect','top-head','top-hair-'+side)
        for name,cx in (('left',10),('right',38)):
            self.add_arc(name+'-head-a',(cx-4,33),(cx-5,30),radius_x=5)
            self.add_arc(name+'-head-top',(cx-5,30),(cx+5,30),radius_x=5)
            self.add_arc(name+'-head-b',(cx+5,30),(cx+4,33),radius_x=5)
            self.add_line(name+'-neck-right',(cx+4,33),(cx+4,36))
            self.add_arc(name+'-shoulder-right',(cx+4,36),(cx+6,38),radius_x=2)
            self.add_line(name+'-side-right',(cx+6,38),(cx+6,40))
            self.add_line(name+'-base',(cx+6,40),(cx-6,40))
            self.add_line(name+'-side-left',(cx-6,40),(cx-6,38))
            self.add_arc(name+'-shoulder-left',(cx-6,38),(cx-4,36),radius_x=2)
            self.add_line(name+'-neck-left',(cx-4,36),(cx-4,33))
            self.add_contour(name,*[name+s for s in ('-head-a','-head-top','-head-b','-neck-right','-shoulder-right','-side-right','-base','-side-left','-shoulder-left','-neck-left')],closed=True)
            self.add_polyline(name+'-fringe',(cx-5,30),(cx,32),(cx+5,30))
            self.relate('connect',name,name+'-fringe')
