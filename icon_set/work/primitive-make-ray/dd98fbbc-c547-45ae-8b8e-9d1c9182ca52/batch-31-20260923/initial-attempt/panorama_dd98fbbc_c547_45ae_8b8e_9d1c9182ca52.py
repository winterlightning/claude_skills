from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dd98fbbc-c547-45ae-8b8e-9d1c9182ca52'
SOURCE_PATH = 'icon_set/work/todo-references/panorama_dd98fbbc-c547-45ae-8b8e-9d1c9182ca52.svg'
AUTHOR = 'gpt-6'
PLAN = 'Panoramic picture frame containing a sun and two overlapping mountain peaks.'
CONSTRUCTION_REFERENCES = 'monitor: equal-radius frame corners.'
OMISSIONS = 'One descending hidden mountain edge removed at the overlap.'

class Drawing(Solo48):
    icon_id = 'panorama'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('panorama',)

    def circle(self, name, cx, cy, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; members.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')

    def build(self):
        self.box('frame',6,6,36,36,4)
        self.circle('sun',17,17,3)
        self.add_polyline('front-mountain',(6,36),(17,25),(28,36));self.relate('connect','frame','front-mountain')
        self.add_polyline('back-mountain',(23,31),(32,20),(42,30));self.relate('connect','front-mountain','back-mountain');self.relate('connect','frame','back-mountain')
