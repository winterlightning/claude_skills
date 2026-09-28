"""A woman with long hair is centered above two men with curved fringes. Lucide users-round informs the triangle and repeated busts. Tiny eyes and ears are omitted; lower fringes are curved instead of pointed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c468c302-cf16-44e6-8780-b21dc169190b'
SOURCE_PATH = 'pictographic-primitives/users/user multiple half female male_c468c302-cf16-44e6-8780-b21dc169190b.svg'
AUTHOR = 'gpt-6'


class WomanAboveTwoMen(Solo48):
    icon_id = 'woman-above-two-men'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('group', 'team', 'woman', 'men', 'users', 'people', 'leader', 'mixed')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def small_bust(self,name,cx,woman):
        # Shared r5 heads, neck nodes on a 3-4-5 triangle, and identical shoulders.
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
        if woman:
            self.add_polyline(name+'-fringe',(cx-5,30),(cx,32),(cx+5,30))
        else:
            self.add_arc(name+'-fringe',(cx-5,30),(cx+5,30),radius_x=7,sweep=False)
        self.relate('connect',name,name+'-fringe')


    def build(self) -> None:
        # Landscape centerline extremes (6,8)-(42,40).
        self.circle('top-head',24,14,6)
        self.add_line('top-fringe',(18,14),(30,14))
        self.relate('connect','top-head','top-fringe')
        for side,d in (('left',-1),('right',1)):
            self.add_line('top-hair-'+side,(24+d*6,14),(24+d*7,18))
            self.relate('connect','top-head','top-hair-'+side)
        for name,cx in (('left',10),('right',38)):
            self.small_bust(name,cx,woman=False)
