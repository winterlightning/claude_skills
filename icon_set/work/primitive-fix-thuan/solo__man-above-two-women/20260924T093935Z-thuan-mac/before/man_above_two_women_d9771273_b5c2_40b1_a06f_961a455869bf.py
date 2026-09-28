"""A plain-headed man with a short shoulder arch sits above two women with fringes. Lucide users-round informs the triangular grouping. Lower hair curls, eyes, and ears are reduced while keeping the pointed fringes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9771273-b5c2-40b1-a06f-961a455869bf'
SOURCE_PATH = 'pictographic-primitives/users/user multiple half male female_d9771273-b5c2-40b1-a06f-961a455869bf.svg'
AUTHOR = 'gpt-6'


class ManAboveTwoWomen(Solo48):
    icon_id = 'man-above-two-women'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('group', 'team', 'man', 'women', 'users', 'people', 'leader', 'mixed')

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
        self.circle('top-head',24,13,5)
        self.add_arc('top-shoulder-left',(20,21),(24,18),radius_x=4,radius_y=3)
        self.add_arc('top-shoulder-right',(24,18),(28,21),radius_x=4,radius_y=3)
        self.add_contour('top-shoulders','top-shoulder-left','top-shoulder-right')
        self.relate('connect','top-head','top-shoulders')
        for name,cx in (('left',10),('right',38)):
            self.small_bust(name,cx,woman=True)
