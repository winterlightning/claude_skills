from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4'
SOURCE_PATH = 'icon_set/work/todo-references/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg'
AUTHOR = 'gpt-6'
PLAN = 'Pig head facing an apple pictured on a rectangular panel. Preserve the overlapping snout.'
CONSTRUCTION_REFERENCES = 'No useful exact Lucide match; source supplies pig/apple arrangement.'
OMISSIONS = 'Tiny nostril and panel portion behind snout omitted.'

class Drawing(Solo48):
    icon_id = 'outdoors-pig-apple'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('outdoors', 'pig', 'apple')

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
        self.add_polyline('panel',(22,25),(22,6),(42,6),(42,38),(24,38))
        self.add_bezier('pig-lower',(6,42),((10,36),(12,33),(20,31)),((21,30),(22,27),(22,25)))
        self.add_bezier('pig-upper',(22,25),((16,24),(13,21),(11,17)),((9,14),(7,14),(6,14)),((6,18),(7,20),(9,21)))
        self.add_contour('pig','pig-lower','pig-upper')
        self.relate('connect','panel','pig')
        self.add_bezier('apple',(32,21),((28,18),(25,20),(26,25)),((27,31),(30,32),(32,30)),((34,32),(37,31),(38,25)),((39,20),(36,18),(32,21)))
        self.add_line('apple-stem',(32,21),(34,16));self.relate('connect','apple','apple-stem')

KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)
KEYSHAPE_REASON = 'The full composition is approximately square and uses the 36×36 centerline envelope.'
